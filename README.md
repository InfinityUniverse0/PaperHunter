# 🕵️‍♂️ PaperHunter

```
 ▄         ▄  ▄         ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌     ▐░▌     ▐░▌          ▐░▌     ▐░▌  
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
```

> PaperHunter is a robust academic paper discovery and precision filtering tool that fetches research from over 300 top computer science conferences via [DBLP](https://dblp.org).

---

## ✨ Features

- 🔍 **Conference Coverage**: Supports 300+ CS conferences across AI, ML, Systems, Networking, Security, Databases...
- 🧠 **Advanced Filtering**: Use logical `AND`/`OR` with keywords for precise search
- 📆 **Multi-Year Query**: Easily search across a year range
- 🔁 **Robust Crawling**: Retry & delay mechanisms to respect DBLP
- 🛠 **Easy to Use**: Advanced CLI with optional legacy mode

---

## 🎓 Supported Conferences

- **Artificial Intelligence**: AAAI, NeurIPS, ICML, CVPR, ICCV, etc.
- **Systems & Architecture**: ASPLOS, ISCA, MICRO, OSDI, SOSP, etc.
- **Networking**: SIGCOMM, NSDI, INFOCOM, MobiCom, etc.
- **Security & Cryptography**: CCS, USENIX Security, NDSS, Eurocrypt, etc.
- **Databases**: SIGMOD, VLDB, ICDE, KDD, etc.

👉 See full list of supported conferences:
```bash
paperhunter conference
```
This will output a list of supported conferences, showing their abbreviation (used in `-con`) and full name.

---

## ⚙️ Installation

### Prerequisites

- Python ≥ 3.6  
- Required packages: `requests`, `beautifulsoup4`

### Steps

#### Clone repo

```bash
git clone https://github.com/yourusername/paperhunter.git
cd paperhunter
```

#### Install

```bash
chmod +x install.sh
./install.sh
```



---

## 🚀 Usage

### ✅ Advanced Mode (Recommended)

```bash
paperhunter -con <conf1> [<conf2> ...] -year <year>|<start>-<end> [-kw <kw1> ...] [-kw_all <kw1> ...]
```

| Flag      | Description                                      |
|-----------|--------------------------------------------------|
| `-con`    | One or more conference abbreviations (or `all`)  |
| `-year`   | A specific year or a range (e.g., `2021-2023`)   |
| `-kw`     | At least one keyword must appear (OR)            |
| `-kw_all` | All keywords must appear (AND)                   |

### 🔍 Examples: Searching Cybersecurity Papers from NDSS, S&P, USENIX Security and CCS

#### 1. Search for "vulnerability" or "malware" papers in **NDSS** and **USENIX Security** (2021–2024):

```bash
paperhunter -con ndss security -year 2021-2024 -kw "vulnerability" "malware"
```

#### 2. Search **IEEE S&P (Oakland)** 2023 papers that **must include** "attack" and at least one of ["IoT", "firmware"]:

```bash
paperhunter -con sp -year 2023 -kw "IoT" "firmware" -kw_all "attack"
```

#### 3. Find papers in **CCS** (ACM Conference on Computer and Communications Security) from 2020 to 2022 related to "side channel":

```bash
paperhunter -con ccs -year 2020-2022 -kw "side channel"
```

#### 4. Search all supported conferences for "DNS hijacking" in the year 2024:

```bash
paperhunter -con all -year 2024 -kw "DNS hijacking"
```


---

### 🕹 Legacy Mode (Simple Syntax)

```bash
paperhunter <conf1> [<conf2> ...] <year>|<start>-<end> <kw1> [<kw2> ...]
```

#### Example

```bash
paperhunter sigmod vldb 2022-2023 "graph database" "query optimization"
```

---

### 🛠 Special Commands

Show help:
```bash
paperhunter help
```

List all supported conferences:
```bash
paperhunter conference
```

---

## 📄 Output Format

- ✅ Status updates per conference/year
- 📊 Total number of matched papers
- 📄 Detailed list with:
  - Conference
  - Year
  - Paper title

---

## ⚠️ Notes

- Randomized delays and retry logic protect DBLP from aggressive crawling
- Conference data depends on DBLP URL patterns (with fallback logic)
- Keyword matching is case-insensitive
- Large-scale queries (e.g., `all` + `2020-2024`) take time ⏱

---

## 📜 License

This project is released under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Powered by [DBLP Computer Science Bibliography](https://dblp.org/)
- Conference list curated from top-tier venues across computer science domains
