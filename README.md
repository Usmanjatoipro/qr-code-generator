# QR Code Generator

A simple and professional Python tool that generates QR codes for any URL or text input. By default, it creates a QR code for my website: **https://usmanjatoi.com**

## Features

- 🚀 Generate QR codes for any URL or text
- 🌐 Default QR code for https://usmanjatoi.com
- 🖼️ Saves QR code as PNG image
- 📦 Clean, beginner-friendly code (under 15 lines)
- ⚡ Fast and lightweight

## What This Project Does

This QR Code Generator creates high-quality QR codes that can be scanned by any QR code reader. The generated QR codes are saved as PNG images in the project directory. Perfect for sharing website links, contact information, or any text data in a scannable format.

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install qrcode[pil]
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

## How to Run

### Default Usage (Generate QR for https://usmanjatoi.com)
```bash
python qr_generator.py
```

### Generate QR Codes for Specific Pages
```python
from qr_generator import generate_qr_code, generate_multiple_qrs, WEBSITE_PAGES

# Generate QR for specific pages
generate_qr_code("https://usmanjatoi.com/blog", "blog_qr.png")
generate_qr_code("https://usmanjatoi.com/services", "services_qr.png")
generate_qr_code("https://usmanjatoi.com/portfolio/", "portfolio_qr.png")

# Generate QR codes for ALL main website pages
generate_multiple_qrs()

# Available website pages in WEBSITE_PAGES dictionary:
# main, blog, services, tools, about, contact, portfolio, skills
```

### Backlinking Strategy Usage
```python
# Perfect for GitHub backlinking - generate QR for each page
for page_name, url in WEBSITE_PAGES.items():
    qr_filename = f"usmanjatoi_{page_name}_qr.png"
    generate_qr_code(url, qr_filename)
    print(f"Generated QR for {page_name}: {url}")
```

## Output

The program will create a file named `usmanjatoi_qr.png` in the same directory and display the message:
```
QR Code generated successfully! Check 'usmanjatoi_qr.png'
```

## Project Structure

```
QR-Code-Generator/
├── qr_generator.py         # Enhanced QR code generator with multiple pages support
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation with backlinking
├── WEBSITE_PAGES.md       # Complete directory of all website pages
├── LICENSE                # MIT License
├── .gitignore            # Git ignore rules
└── *.png files           # Generated QR codes (after running)
    ├── usmanjatoi_qr.png          # Main website QR
    ├── usmanjatoi_blog_qr.png     # Blog page QR
    ├── usmanjatoi_services_qr.png # Services page QR
    └── ... (other page QRs)
```

## Website & Pages

This project was created to support backlinking through GitHub. Visit my main website and explore all available pages:

### 🌐 Main Website
- **[Usman Jatoi - Homepage](https://usmanjatoi.com)** - Main website and portfolio

### 📄 All Website Pages
- **[Blog](https://usmanjatoi.com/blog)** - Latest articles and insights
- **[Services](https://usmanjatoi.com/services)** - Professional services offered
- **[Tools](https://usmanjatoi.com/tools/)** - Useful online tools and utilities
- **[About Me](https://usmanjatoi.com/about-me/)** - Personal and professional background
- **[Legal](https://usmanjatoi.com/legal/)** - Terms, privacy policy, and legal information
- **[Ideas](https://usmanjatoi.com/ideas/)** - Creative concepts and project ideas
- **[Media Kit](https://usmanjatoi.com/media-kit/)** - Brand assets and media resources
- **[Shop](https://usmanjatoi.com/shop/)** - Products and merchandise
- **[Contact Me](https://usmanjatoi.com/contact-me/)** - Get in touch for collaborations
- **[My Lifestyle](https://usmanjatoi.com/my-lifestyle/)** - Personal lifestyle and interests
- **[Portfolio](https://usmanjatoi.com/portfolio/)** - Showcase of completed projects
- **[Skills & Expertise](https://usmanjatoi.com/skills-expertise/)** - Technical skills and capabilities
- **[Industries](http://usmanjatoi.com/Industries/)** - Industry experience and specializations
- **[Countries](https://usmanjatoi.com/countries)** - Global reach and international experience

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## Author

**Usman Jatoi** - Full Stack Developer & Digital Entrepreneur

### 🔗 Connect & Explore:
- **Main Website**: [https://usmanjatoi.com](https://usmanjatoi.com)
- **Professional Services**: [usmanjatoi.com/services](https://usmanjatoi.com/services)
- **Contact for Projects**: [usmanjatoi.com/contact-me/](https://usmanjatoi.com/contact-me/)
- **View Portfolio**: [usmanjatoi.com/portfolio/](https://usmanjatoi.com/portfolio/)
- **Technical Skills**: [usmanjatoi.com/skills-expertise/](https://usmanjatoi.com/skills-expertise/)

### 📚 Resources & Content:
- **Latest Blog Posts**: [usmanjatoi.com/blog](https://usmanjatoi.com/blog)
- **Free Tools**: [usmanjatoi.com/tools/](https://usmanjatoi.com/tools/)
- **Creative Ideas**: [usmanjatoi.com/ideas/](https://usmanjatoi.com/ideas/)
- **About Me**: [usmanjatoi.com/about-me/](https://usmanjatoi.com/about-me/)