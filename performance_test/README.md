# Performance Testing EduQuiz

Dokumen ini menjelaskan pengujian performa untuk proyek EduQuiz. Tujuannya untuk memastikan fungsi-fungsi utama berjalan secara efisien dan optimal.

## 🧪 Fungsi yang Diuji
1. **`load_quiz_data`**: Memuat data soal dari file `kuis_table.py`.
2. **`evaluate_answer`**: Mengevaluasi jawaban pengguna.
3. **`calculate_score`**: Menghitung skor akhir.
4. **`start_quiz`**: Menjalankan keseluruhan kuis (dengan simulasi input pengguna).

## 📋 Alat dan Teknik
- **Python Modules**: `timeit`.
- **Pengulangan**: Fungsi diuji dalam beberapa iterasi untuk mengukur konsistensi performa.
- **Mocking**: `unittest.mock.patch` digunakan untuk mensimulasikan input pengguna pada fungsi `start_quiz`.

## 🧑‍💻 Konfigurasi Pengujian
- **Penguji**: Hamid Khaeruman
- **Tanggal Pengujian**: 6 Mei 2025

## 📊 Hasil Pengujian

Hasil pengujian performa dicatat dalam hitungan detik. Semua fungsi diuji untuk memastikan waktu eksekusi optimal.

| Fungsi               | Iterasi | Waktu Eksekusi (detik) | Keterangan                                                                                                                                |
|-----------------------|---------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `load_quiz_data`      | 6       | 0.0017                 | Waktu untuk memuat data kuis dari file. Semakin kecil nilainya, semakin cepat.                                                              |
| `evaluate_answer`     | 6       | 0.0000                 | Waktu untuk mengevaluasi jawaban pengguna. Semakin kecil nilainya, semakin cepat.                                                          |
| `calculate_score`     | 6       | 0.0000                 | Waktu untuk menghitung skor akhir kuis. Semakin kecil nilainya, semakin cepat.                                                              |
| `start_quiz`          | 6       | 0.0140                 | Waktu untuk menjalankan seluruh alur kuis dengan simulasi input pengguna. Semakin kecil nilainya, semakin cepat.                           |

## 🔧 Kesimpulan

- Semua fungsi berjalan optimal untuk *use case* normal.
- Fungsi `load_quiz_data` memiliki waktu eksekusi yang sangat cepat.
- Fungsi `evaluate_answer` dan `calculate_score` memiliki waktu eksekusi yang sangat singkat karena operasinya sederhana.
- Fungsi `start_quiz` diuji dengan simulasi input pengguna dan menunjukkan performa yang memadai.

## 📝 Catatan Tambahan

- Hasil pengujian ini diperoleh dengan konfigurasi tertentu dan dapat bervariasi tergantung pada lingkungan eksekusi (misalnya, spesifikasi perangkat keras, sistem operasi, versi Python).
- Untuk pengujian `start_quiz`, simulasi input pengguna dilakukan menggunakan `unittest.mock.patch`.