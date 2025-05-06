import json
import os
from typing import Dict, Any, Optional

class ConfigLoader:
    """
    Kelas untuk menangani pemuatan konfigurasi runtime dengan teknik defensive programming.
    Mengimplementasikan pola konstruksi konfigurasi runtime.
    """
    
    def __init__(self, config_file: str = 'soal_config.json'):
        """
        Inisialisasi ConfigLoader dengan file konfigurasi.
        
        Args:
            config_file: Nama file konfigurasi JSON
        """
        self.config_file = os.path.join(os.path.dirname(__file__), config_file)
        self._config_data = None
        self._last_modified = 0
        
    def _validate_config(self, config: Any) -> bool:
        """
        Validasi struktur konfigurasi.
        
        Args:
            config: Data konfigurasi yang dimuat
            
        Returns:
            bool: True jika konfigurasi valid, False jika tidak
        """
        if not isinstance(config, list):
            return False
            
        required_keys = {'category', 'question', 'answer'}
        for item in config:
            if not isinstance(item, dict):
                return False
            if not required_keys.issubset(item.keys()):
                return False
            if not all(isinstance(item[key], str) for key in required_keys):
                return False
                
        return True
    
    def _load_config_file(self) -> Optional[Dict]:
        """
        Memuat dan mengurai file konfigurasi dengan aman.
        
        Returns:
            Optional[Dict]: Data konfigurasi yang diurai atau None jika terjadi kesalahan
        """
        try:
            # Periksa apakah file ada dan dapat dibaca
            if not os.path.exists(self.config_file):
                raise FileNotFoundError(f"File konfigurasi tidak ditemukan: {self.config_file}")
            if not os.access(self.config_file, os.R_OK):
                raise PermissionError(f"Tidak ada izin baca untuk file: {self.config_file}")
                
            # Dapatkan waktu modifikasi terakhir untuk potensi caching
            current_modified = os.path.getmtime(self.config_file)
            
            # Hanya muat ulang jika file telah berubah atau belum dimuat
            if self._config_data is None or current_modified > self._last_modified:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    
                if not self._validate_config(config):
                    raise ValueError("Struktur konfigurasi tidak valid")
                    
                self._config_data = config
                self._last_modified = current_modified
                
            return self._config_data
            
        except json.JSONDecodeError as e:
            print(f"Error mengurai konfigurasi JSON: {e}")
        except (FileNotFoundError, PermissionError, ValueError) as e:
            print(f"Kesalahan konfigurasi: {e}")
        except Exception as e:
            print(f"Kesalahan tak terduga saat memuat konfigurasi: {e}")
            
        return None
    
    def get_config(self) -> Optional[Dict]:
        """
        Metode publik untuk mendapatkan data konfigurasi.
        Mengimplementasikan defensive programming dengan menangani semua kesalahan potensial.
        
        Returns:
            Optional[Dict]: Data konfigurasi atau None jika terjadi kesalahan
        """
        return self._load_config_file()
    
    def get_questions_by_category(self, category: str) -> Optional[list]:
        """
        Dapatkan pertanyaan yang difilter berdasarkan kategori.
        
        Args:
            category: Kategori untuk memfilter pertanyaan
            
        Returns:
            Optional[list]: Daftar pertanyaan dalam kategori atau None jika terjadi kesalahan
        """
        config = self.get_config()
        if config is None:
            return None
            
        try:
            return [q for q in config if q['category'].lower() == category.lower()]
        except Exception as e:
            print(f"Kesalahan saat memfilter pertanyaan berdasarkan kategori: {e}")
            return None

def load_quiz_data() -> Optional[list]:
    """
    Fungsi publik untuk memuat data kuis menggunakan ConfigLoader.
    Mempertahankan kompatibilitas dengan kode yang ada.
    
    Returns:
        Optional[list]: Daftar pertanyaan kuis atau None jika terjadi kesalahan
    """
    loader = ConfigLoader()
    return loader.get_config()