import re
from bs4 import BeautifulSoup
from config import session, MAX_SUBPAGE, KNOWN_CONFS
from utils import random_delay

def check_conf_pages(short, key, year):
    """Check and return valid conference pages for a given year from DBLP"""
    base_url = f"https://dblp.org/db/conf/{short}/"

    # Special suffix mappings for specific conferences with non-standard URL formats
    special_suffix = {
        "vldb": "w",
        "sca": "p",
        "ubicomp": "ap",
        "eurovis": "short",
        "sgp": "p",
        "egsr": "st",
        "pg": "s",
    }

    # 1. Try main conference page (e.g., icml2024.html)
    main_url = f"{base_url}{key}{year}.html"
    try:
        resp = session.get(main_url, timeout=10)
        if resp.status_code == 200:
            return [(main_url, resp.status_code)]
    except Exception as e:
        print(f"[-] Request error for main page: {e}")

    # 2. Try sub-pages (e.g., icml2024-1.html)
    found = []
    for i in range(1, MAX_SUBPAGE + 1):
        sub_url = f"{base_url}{key}{year}-{i}.html"
        try:
            resp = session.get(sub_url, timeout=10)
            if resp.status_code == 200:
                found.append((sub_url, resp.status_code))
            else:
                break  # Stop if non-200 status code encountered
        except Exception as e:
            print(f"[-] Error accessing sub-page {i}: {e}")
            break
        random_delay()  # Avoid aggressive crawling

    if found:
        return found  # Return found sub-pages

    # 3. Try special suffix pages for conferences with unique URL patterns
    if key in special_suffix:
        suffix = special_suffix[key]
        special_url = f"{base_url}{key}{year}{suffix}.html"
        try:
            resp = session.get(special_url, timeout=10)
            if resp.status_code == 200:
                return [(special_url, resp.status_code)]
        except Exception as e:
            print(f"[-] Error accessing special suffix page: {e}")

    # No valid pages found
    return []

def fetch_papers(conf_short, year, keywords_any, keywords_all):
    """Fetch and filter papers from a conference for a specific year based on keyword criteria"""
    conf_info = KNOWN_CONFS.get(conf_short.lower())
    if not conf_info:
        print(f"[!] Unknown conference abbreviation `{conf_short}`. Use 'conference' command to see supported list.")
        return []
    
    full_name, dblp_key = conf_info
    print(f"[*] Recognized conference: {full_name}")
    
    # Get valid conference pages using the page checking logic
    valid_pages = check_conf_pages(conf_short, dblp_key, year)
    
    if not valid_pages:
        print(f"[!] No valid conference pages found for {full_name} in {year}")
        return []
    
    # Extract all paper titles from valid pages
    titles = []
    for url, status in valid_pages:
        try:
            resp = session.get(url, timeout=10)
            if resp.status_code != 200:
                print(f"[!] Failed to retrieve {url} (Status code: {resp.status_code})")
                continue
            
            # Parse HTML content to extract paper titles
            soup = BeautifulSoup(resp.text, "html.parser")
            for cite in soup.find_all("cite", class_="data"):
                title_tag = cite.find("span", class_="title")
                if title_tag and title_tag.text:
                    titles.append(title_tag.text.strip())
            
            # Add random delay to prevent overwhelming the server
            random_delay()
        except Exception as e:
            print(f"[!] Error during content extraction: {e}")
    
    # Filter titles based on keyword criteria
    matched_titles = []
    for title in titles:
        # Check if all required keywords (kw_all) are present
        all_match = True
        if keywords_all:
            for kw in keywords_all:
                if not re.search(kw, title, re.IGNORECASE):
                    all_match = False
                    break
            if not all_match:
                continue
        
        # Check if at least one optional keyword (kw) is present
        any_match = True
        if keywords_any:
            has_matching_kw = False
            for kw in keywords_any:
                if re.search(kw, title, re.IGNORECASE):
                    has_matching_kw = True
                    break
            any_match = has_matching_kw
        
        # Include title if it meets all criteria
        if all_match and any_match:
            matched_titles.append(title)
    
    print(f"[*] Crawled {len(titles)} total papers. Found {len(matched_titles)} matching the criteria.")
    return matched_titles