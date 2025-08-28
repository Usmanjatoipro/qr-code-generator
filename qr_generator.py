#!/usr/bin/env python3
"""
QR Code Generator for Usman Jatoi's Website
Generates QR codes for any URL or text with focus on website backlinking.
Default: https://usmanjatoi.com

Usage Examples:
- generate_qr_code()  # Main website
- generate_qr_code("https://usmanjatoi.com/blog")  # Blog page
- generate_qr_code("https://usmanjatoi.com/services")  # Services page
"""

import qrcode
from PIL import Image

# Website pages for easy reference
WEBSITE_PAGES = {
    "main": "https://usmanjatoi.com",
    "blog": "https://usmanjatoi.com/blog",
    "services": "https://usmanjatoi.com/services", 
    "tools": "https://usmanjatoi.com/tools/",
    "about": "https://usmanjatoi.com/about-me/",
    "contact": "https://usmanjatoi.com/contact-me/",
    "portfolio": "https://usmanjatoi.com/portfolio/",
    "skills": "https://usmanjatoi.com/skills-expertise/"
}

def generate_qr_code(text="https://usmanjatoi.com", filename="usmanjatoi_qr.png"):
    """Generate QR code for given text or default website."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code generated successfully! Check '{filename}'")
    print(f"QR Code contains: {text}")

def generate_multiple_qrs():
    """Generate QR codes for all main website pages."""
    for page_name, url in WEBSITE_PAGES.items():
        filename = f"usmanjatoi_{page_name}_qr.png"
        generate_qr_code(url, filename)

if __name__ == "__main__":
    # Generate main website QR code
    generate_qr_code()