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

> A powerful crawler & filtering tool for academic papers from top-tier computer science conferences via [DBLP](https://dblp.org).

---

## ✨ Features

- 🔍 **Conference Coverage**: Supports 200+ CS conferences across AI, ML, Systems, Networking, Security, Databases...
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
python main.py conference
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

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### `requirements.txt` content

```text
requests>=2.25.1
beautifulsoup4>=4.9.3
```

---

## 🚀 Usage

### ✅ Advanced Mode (Recommended)

```bash
python main.py -con <conf1> [<conf2> ...] -year <year>|<start>-<end> [-kw <kw1> ...] [-kw_all <kw1> ...]
```

| Flag      | Description                                      |
|-----------|--------------------------------------------------|
| `-con`    | One or more conference abbreviations (or `all`)  |
| `-year`   | A specific year or a range (e.g., `2021-2023`)   |
| `-kw`     | At least one keyword must appear (OR)            |
| `-kw_all` | All keywords must appear (AND)                   |

#### Examples

Search for "object detection" papers in CVPR & ICCV (2020–2023):

```bash
python main.py -con cvpr iccv -year 2020-2023 -kw "object detection"
```

Find NeurIPS 2022 papers with "deep learning" AND at least one of ["object detection", "image segmentation"]:

```bash
python main.py -con neurips -year 2022 -kw "object detection" "image segmentation" -kw_all "deep learning"
```

Search all conferences for "quantum computing" papers (2021–2023):

```bash
python main.py -con all -year 2021-2023 -kw "quantum computing"
```

---

### 🕹 Legacy Mode (Simple Syntax)

```bash
python main.py <conf1> [<conf2> ...] <year>|<start>-<end> <kw1> [<kw2> ...]
```

#### Example

```bash
python main.py sigmod vldb 2022-2023 "graph database" "query optimization"
```

---

### 🛠 Special Commands

Show help:
```bash
python main.py help
```

List all supported conferences:
```bash
python main.py conference
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
