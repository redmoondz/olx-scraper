"""
Конфигурация для OLX scraper
"""
import os

# Базовый путь проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# API настройки

base_url = "https://www.olx.ua/apigateway/graphql"

# Учетные данные
headers = {
  'Cookie': 'PHPSESSID=p27bgldl1phjn3oa1a7dn7fsji',
  'Content-Type': 'application/json',
  'accept-language': 'uk',
  'authorization': 'Bearer eyJraWQiOiI3TzI5clpiaDVHXC9SR3NTZ2g2ZzZRN1QrMVJZdTdsWFwvXC9qd3dyWnozVjNzPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIyMGZkNDljNi1hZDBiLTRiMjItOGYzZC05NWUyYjZmYjI2OTgiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtd2VzdC0xLmFtYXpvbmF3cy5jb21cL2V1LXdlc3QtMV9WMkFKVVgwWEUiLCJjbGllbnRfaWQiOiIzMDlsc2doMGRlaXJsbzJsYTlrbXJtaGUzdiIsIm9yaWdpbl9qdGkiOiJjYzBkNzM4ZC03NDZkLTQyOWYtYTg3ZC01YTlhNWRhMGJmMDAiLCJldmVudF9pZCI6IjE0YTU2MjA3LWVhYmMtNGRjYy1hNDRiLWNhMGY2ZDU3YmM1NCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3NjI2MzcxNzUsImV4cCI6MTc2MjYzODk1NSwiaWF0IjoxNzYyNjM4MDU1LCJqdGkiOiJkMWFlNDJmYy0zZjk3LTQ1NDYtYmM3NS00NmI5YWU0OTZkZWYiLCJ1c2VybmFtZSI6IjU1NTljMDU5LWMyYzItNDUzMS04MzQxLWEwZGNhNjI1ZDRlNyJ9.PRL5aOyPN1w-9DDmLidXegulTHCQ5YeHki0wf2TEtxn41ZPcnXR6szZIg05cuoFEHcIBqAlEQ6KLKbEnhWCx5s8uPdl-p6HkS-i1-BUXPqjhJ7fg5C7aInCryI8qqqc1PIrB0Qz1TN2gIonvr3yHi2jsZTtj-4U_tO-WFu-PzVJT0wRK7fmRpyBLsAPicC6nqeqz0a2TwYlWtD5ErMiMv3ePIz_NqPyqwN1aT-sHJqwQZss3j1F3NZSAk7J_tTQtS2ii-r-ZXPmW1nFYZ8vF-s507AVo50twfmdIeV0Mm3y7Tvy93Ht_kI8h5RZBTrywcSitih689v3C8xqtqIfuXw',
  'content-type': 'application/json',
  'origin': 'https://www.olx.ua',
  'priority': 'u=1, i',
  'referer': 'https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/dnepr/q-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%B0-%D0%BE%D1%80%D0%B5%D0%BD%D0%B4%D0%B0/?currency=UAH&search%5Bprivate_business%5D=private&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=10000&search%5Bfilter_float_price:to%5D=15000&search%5Bfilter_float_floor:from%5D=2&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_float_total_area:from%5D=30&search%5Bfilter_float_total_area:to%5D=60&search%5Bfilter_enum_furnish%5D%5B0%5D=yes&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=dvuhkomnatnye&search%5Bfilter_enum_number_of_rooms_string%5D%5B1%5D=odnokomnatnye',
  'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'x-client': 'DESKTOP'
}

# Настройки логирования
log_level = "DEBUG"  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Директории

log_dir = os.path.join(BASE_DIR, "logs")
data_dir = os.path.join(BASE_DIR, "data")
cache_dir = os.path.join(BASE_DIR, "cache")


max_concurrent_requests = 5
timeout_between_request = 2  # в секундах
timeout_when_error = 30  # в секундах
retry_attempts = 3