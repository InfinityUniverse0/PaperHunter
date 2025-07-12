import sys
import time
import random
from config import KNOWN_CONFS, DELAY_RANGE

def print_help():
    """Print detailed usage information and parameter descriptions"""
    print("=== Conference Paper Crawler Usage Guide ===")
    print("\nA. Advanced Usage (Recommended):")
    print("   python3 main.py -con <conf1> [<conf2> ...] -year <year>|<start_year>-<end_year> [-kw <kw1> ...] [-kw_all <kw1> ...]")
    print("   Example:")
    print("   python3 main.py -con cvpr iccv -year 2020-2023 -kw object detection -kw_all deep learning")
    print("   (Requires 'deep' and 'learning' to appear together, plus at least one of 'object' or 'detection')")
    
    print("\nB. Legacy Usage (Simple Syntax):")
    print("   python3 main.py <conf1> [<conf2> ...] <year>|<start_year>-<end_year> <keyword1> [<keyword2> ...]")
    
    print("\nC. Special Commands:")
    print("   1. Search All Conferences:")
    print("      python3 main.py all <year>|<start_year>-<end_year> <keyword1> [<keyword2> ...]")
    
    print("   2. Show This Help:")
    print("      python3 main.py help")
    
    print("   3. List Supported Conferences:")
    print("      python3 main.py conference")
    
    print("\n=== Parameter Descriptions ===")
    print("<conf>            : Conference abbreviations (e.g., cvpr, ndss)")
    print("<year>            : Single year (e.g., 2023) or year range (e.g., 2020-2023)")
    print("-kw <keyword>     : Keywords (at least one must appear, case-insensitive)")
    print("-kw_all <keyword> : Keywords (all must appear simultaneously, case-insensitive)")
    
    sys.exit(0)

def list_conferences():
    """List all supported conferences with their abbreviations and full names"""
    print("=== Supported Conferences ===")
    print("{:<20} {:<100}".format("Abbreviation", "Full Name"))
    print("-" * 90)
    
    for short, (full, key) in sorted(KNOWN_CONFS.items()):
        print("{:<20} {:<100}".format(short, full))
    
    print(f"\nTotal: {len(KNOWN_CONFS)} conferences")
    sys.exit(0)

def random_delay():
    """Add random delay to avoid aggressive crawling"""
    time.sleep(random.uniform(*DELAY_RANGE))