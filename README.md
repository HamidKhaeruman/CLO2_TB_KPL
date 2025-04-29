# EduQuiz – Aplikasi Kuis Edukasi CLI

EduQuiz adalah aplikasi kuis berbasis command-line yang dikembangkan untuk memenuhi tugas besar CLO2 mata kuliah Konstruksi Perangkat Lunak. Aplikasi ini dirancang untuk membantu pengguna berlatih menjawab soal-soal edukatif berdasarkan kategori dan tingkat kesulitan tertentu.

## 👨‍👩‍👦‍👦 Anggota Tim
| Nama Lengkap                                | NIM         |
|---------------------------------------------|-------------|
| Adhiansyah Muhammad Pradana Farawowan       | 2211104038  |
| Hamid Khaeruman                             | 2211104040  |
| Ricky Revenando                             | 2211104047  |
| Dava Ardana Valdiaswara Ali                 | 2211104048  |

## 🧱 Struktur Proyek
<pre>
/CLO2_TB_KPL
├── main.py
├── README.md
├── subfolder_A  ← dikerjakan oleh Adhiansyah & Dava
│   ├── config_loader.py    ← runtime configuration
│   ├── kuis_table.py       ← implementasi table-driven
│   └── soal_config.json
└── subfolder_B  ← dikerjakan oleh Ricky & Hamid
    ├── automata_engine.py  ← state machine untuk navigasi kuis
    └── question_utils.py   ← code reuse: library soal dan evaluasi
</pre>

## 🔧 Teknologi & Teknik Konstruksi

- **Bahasa**: Python
- **Teknik Konstruksi yang Digunakan**:
  - Table-driven Construction (Adhiansyah & Dava)
  - Runtime Configuration (Adhiansyah & Dava)
  - Automata (Ricky & Hamid)
  - Code Reuse / Library (Ricky & Hamid)
- **Praktik Pengembangan**:
  - Unit Testing per modul
  - Performance Testing (terutama modul load dan evaluasi)
  - Defensive Programming / Design by Contract

## 🚀 Cara Menjalankan Aplikasi

```bash
python main.py
