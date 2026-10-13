import requests
import re
import threading
import time 
import os
from datetime import datetime
from collections import Counter


class EmailExtractor:
    """Enterprise-level Email Extraction System"""
    
    def __init__(self, url, output_file="leads.txt", log_file="extraction_log.txt"):
        self.url = url
        self.output_file = output_file
        self.log_file = log_file
        self.email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        self.extracted_emails = set()  # Use set to avoid duplicates
        self.session = requests.Session()  # Reuse connection for better performance
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        
    def log_message(self, message):
        """Log messages to file and console"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        
        try:
            # FIXED: Use UTF-8 encoding to handle special characters
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception as e:
            print(f"Warning: Could not write to log file: {e}")
    
    def get_emails_from_url(self):
        """Fetch and extract emails from the target URL"""
        try:
            self.log_message(f"Fetching: {self.url}")
            
            response = self.session.get(self.url, timeout=10)
            
            if response.status_code == 200:
                self.log_message("Connection successful (Status 200)")
                
                raw_html = response.text
                
                # DEBUG: Save raw HTML to file for inspection
                with open("debug_html.txt", "w", encoding="utf-8") as f:
                    f.write(raw_html)
                
                found_emails = re.findall(self.email_pattern, raw_html)
                
                # Remove duplicates and convert to lowercase for consistency
                unique_emails = set(email.lower() for email in found_emails)
                
                self.log_message(f"Found {len(unique_emails)} unique email(s)")
                
                # DEBUG: If no emails found, show what we searched
                if not unique_emails:
                    self.log_message("NOTE: No emails in static HTML (may be loaded by JavaScript)")
                    self.log_message("For JS-rendered sites, consider using Selenium")
                
                return unique_emails
            
            elif response.status_code == 429:
                self.log_message("Rate Limited (429) - Waiting 30 seconds...")
                time.sleep(30)
                return self.get_emails_from_url()  # Retry after waiting
            
            elif response.status_code == 404:
                self.log_message("Page Not Found (404)")
                return set()
            
            else:
                self.log_message(f"Unexpected Status Code: {response.status_code}")
                return set()
                
        except requests.exceptions.Timeout:
            self.log_message("Connection Timeout - URL took too long to respond")
            return set()
        except requests.exceptions.ConnectionError:
            self.log_message("Connection Error - Check your internet")
            return set()
        except requests.exceptions.RequestException as e:
            self.log_message(f"Request Error: {str(e)}")
            return set()
    
    def load_existing_emails(self):
        """Load previously extracted emails to avoid duplicates"""
        if os.path.exists(self.output_file):
            try:
                with open(self.output_file, "r", encoding="utf-8") as f:
                    for line in f:
                        email = line.strip()
                        if "@" in email:  # Only add valid emails
                            self.extracted_emails.add(email.lower())
                self.log_message(f"Loaded {len(self.extracted_emails)} existing emails")
            except Exception as e:
                self.log_message(f"Warning: Could not load existing emails: {e}")
    
    def save_emails_to_file(self, new_emails):
        """Save emails to file with deduplication"""
        if not new_emails:
            self.log_message("No new emails to save")
            return 0
        
        # Add new emails to existing set
        before_count = len(self.extracted_emails)
        self.extracted_emails.update(new_emails)
        new_count = len(self.extracted_emails) - before_count
        
        try:
            # Write all unique emails sorted with UTF-8 encoding
            with open(self.output_file, "w", encoding="utf-8") as f:
                for email in sorted(self.extracted_emails):
                    f.write(email + "\n")
            
            self.log_message(f"Saved {new_count} new email(s) | Total: {len(self.extracted_emails)}")
            return new_count
            
        except Exception as e:
            self.log_message(f"Error saving to file: {e}")
            return 0
    
    def display_extracted_emails(self):
        """Display all extracted emails in a nice format"""
        if not self.extracted_emails:
            print("\n" + "="*60)
            print("[NO EMAILS FOUND YET]")
            print("="*60)
            return
        
        print("\n" + "="*60)
        print(f"[EXTRACTED EMAILS] ({len(self.extracted_emails)} total)")
        print("="*60)
        for i, email in enumerate(sorted(self.extracted_emails), 1):
            print(f"{i:3d}. {email}")
        print("="*60 + "\n")
    
    def get_statistics(self):
        """Display extraction statistics"""
        if not self.extracted_emails:
            return
        
        # Count domains
        domains = Counter()
        for email in self.extracted_emails:
            domain = email.split("@")[1]
            domains[domain] += 1
        
        print("\n" + "="*60)
        print("[STATISTICS]")
        print("="*60)
        print(f"Total Emails: {len(self.extracted_emails)}")
        print(f"Total Domains: {len(domains)}")
        print("\nTop Domains:")
        for domain, count in domains.most_common(5):
            print(f"  - {domain}: {count}")
        print("="*60 + "\n")
    
    def run_extraction(self):
        """Main extraction process"""
        self.log_message("--- STARTING EMAIL EXTRACTION ---")
        self.log_message(f"Target URL: {self.url}")
        
        self.load_existing_emails()
        new_emails = self.get_emails_from_url()
        saved_count = self.save_emails_to_file(new_emails)
        
        self.display_extracted_emails()
        self.get_statistics()
        
        return saved_count


def background_extraction():
    """Run extraction in background every 30 seconds"""
    extractor = EmailExtractor("https://www.webhouseindia.com/contact-us")
    
    while True:
        extractor.run_extraction()
        print("\n[WAIT] Next extraction in 30 seconds... (Press Ctrl+C to stop)\n")
        time.sleep(30)


def show_help():
    """Display help information"""
    print("\n" + "="*70)
    print("IMPORTANT: JAVASCRIPT-RENDERED CONTENT")
    print("="*70)
    print("""
This extractor works with static HTML. However, modern websites often load
emails dynamically using JavaScript. For such websites, you have options:

1. QUICK FIX: Look at the website's "Contact Us" page directly
   - Check visible text, contact forms, footer sections
   - Some sites show emails in visible form

2. ADVANCED: Use Selenium for JavaScript rendering
   - Selenium simulates a real browser that runs JavaScript
   - Emails loaded by JS will then be visible in the HTML
   
   Install Selenium:
   > pip install selenium
   
   Then use:
   from selenium import webdriver
   driver = webdriver.Chrome()  # Requires ChromeDriver
   driver.get(url)
   html = driver.page_source
   # Now extract emails from rendered HTML
   
3. CURL METHOD: Check HTML comments and AJAX responses
   - Open DevTools (F12) -> Network tab
   - Look for AJAX calls that fetch email data
   - Emails might be in API responses instead of HTML

Current URL: https://www.webhouseindia.com/contact-us
Status: Emails appear to be loaded via JavaScript/AJAX
""")
    print("="*70 + "\n")


def main():
    """Main menu interface"""
    print("\n" + "="*70)
    print("ENTERPRISE EMAIL EXTRACTOR - LEAD GENERATION SYSTEM")
    print("="*70)
    
    url = "https://www.webhouseindia.com/contact-us"
    extractor = EmailExtractor(url)
    
    while True:
        print("\n[1] Extract Emails Now")
        print("[2] View All Extracted Emails")
        print("[3] Show Statistics")
        print("[4] Start Background Extraction (every 30 seconds)")
        print("[5] Show Debug HTML (check debug_html.txt)")
        print("[6] Help - How to handle JavaScript sites")
        print("[7] Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            extractor.run_extraction()
        
        elif choice == "2":
            extractor.load_existing_emails()
            extractor.display_extracted_emails()
        
        elif choice == "3":
            extractor.load_existing_emails()
            extractor.get_statistics()
        
        elif choice == "4":
            print("\nStarting background extraction (Press Ctrl+C to stop)...")
            try:
                background_extraction()
            except KeyboardInterrupt:
                print("\n\nBackground extraction stopped")
                extractor.log_message("Background extraction stopped by user")
        
        elif choice == "5":
            try:
                with open("debug_html.txt", "r", encoding="utf-8") as f:
                    content = f.read()
                    # Show first 2000 characters
                    print("\n" + "="*70)
                    print("DEBUG HTML (first 2000 chars):")
                    print("="*70)
                    print(content[:2000])
                    print("\n... (See debug_html.txt for full content)")
                    print("="*70)
            except FileNotFoundError:
                print("No debug_html.txt found. Run extraction first.")
        
        elif choice == "6":
            show_help()
        
        elif choice == "7":
            print("\nThank you for using Email Extractor!")
            extractor.log_message("Program ended")
            break
        
        else:
            print("Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()

