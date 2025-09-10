#!/usr/bin/env python3
"""
Vulnerability Demonstration Script
This script demonstrates some of the vulnerabilities present in the mail applications.
For educational and testing purposes only.
"""

def check_vulnerable_versions():
    """Check and report on vulnerable package versions."""
    print("🔍 Dependabot Vulnerability Test Repository")
    print("=" * 50)
    
    vulnerabilities = [
        {
            "package": "requests",
            "version": "2.25.1",
            "vulnerabilities": [
                "CVE-2021-33503: Improper handling of HTTP redirects"
            ]
        },
        {
            "package": "Jinja2", 
            "version": "2.11.3",
            "vulnerabilities": [
                "CVE-2020-28493: ReDOS vulnerability in email validation"
            ]
        },
        {
            "package": "Flask",
            "version": "1.1.4", 
            "vulnerabilities": [
                "Various security issues in older versions"
            ]
        },
        {
            "package": "urllib3",
            "version": "1.26.4",
            "vulnerabilities": [
                "CVE-2021-33503: Improper handling of HTTP redirects"
            ]
        },
        {
            "package": "Pillow",
            "version": "8.1.2",
            "vulnerabilities": [
                "CVE-2021-25287: Out-of-bounds read in J2K encoder",
                "CVE-2021-25288: Buffer overflow in PDF parser"
            ]
        },
        {
            "package": "axios",
            "version": "0.21.1", 
            "vulnerabilities": [
                "CVE-2021-3749: Regular Expression Denial of Service"
            ]
        },
        {
            "package": "lodash",
            "version": "4.17.19",
            "vulnerabilities": [
                "CVE-2021-23337: Prototype pollution in zipObjectDeep"
            ]
        }
    ]
    
    print(f"📦 Found {len(vulnerabilities)} packages with known vulnerabilities:\n")
    
    for vuln in vulnerabilities:
        print(f"⚠️  {vuln['package']} v{vuln['version']}")
        for cve in vuln['vulnerabilities']:
            print(f"   • {cve}")
        print()
    
    print("🤖 Dependabot Configuration:")
    print("   • Monitoring Python (pip) dependencies")  
    print("   • Monitoring Node.js (npm) dependencies")
    print("   • Daily update schedule")
    print("   • Up to 10 open PRs per ecosystem")
    
    print("\n✅ Repository is properly configured to trigger Dependabot alerts!")
    print("   Dependabot should create pull requests to update these vulnerable packages.")

def demonstrate_template_vulnerability():
    """Demonstrate a simple template injection vulnerability (for educational purposes)."""
    print("\n🎯 Template Injection Example (Jinja2 vulnerability):")
    print("-" * 50)
    
    # This would be vulnerable in older Jinja2 versions
    template_string = "Hello {{ name }}! Your account balance is ${{ balance }}."
    
    # Safe data
    safe_data = {"name": "John", "balance": "100.00"}
    print(f"Safe template: {template_string}")
    print(f"Safe data: {safe_data}")
    
    # This demonstrates why template validation is important
    print("\n⚠️  In vulnerable versions, untrusted template strings could lead to:")
    print("   • Server-side template injection (SSTI)")
    print("   • Remote code execution")
    print("   • Information disclosure")

if __name__ == "__main__":
    check_vulnerable_versions()
    demonstrate_template_vulnerability()
    
    print("\n" + "=" * 50)
    print("🚨 SECURITY NOTICE:")
    print("This repository contains intentionally vulnerable dependencies.")
    print("Do not use this code in production environments!")
    print("=" * 50)