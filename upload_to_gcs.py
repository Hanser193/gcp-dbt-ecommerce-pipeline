from google.cloud import storage
import pandas as pd
import os

# 1. Configuraciones
BUCKET_NAME = 'brayan-data-lake-olist' 
LOCAL_CSV_PATH = 'data/olist_orders_dataset.csv'
LOCAL_PARQUET_PATH = 'data/olist_orders_dataset.parquet'
DESTINATION_BLOB_NAME = 'raw/orders/olist_orders.parquet'

def upload_to_gcs():
    print("🚀 Iniciando el pipeline de Data Engineering...")
    
    # 2. Transformación básica: CSV a Parquet (Mejor práctica)
    print("📦 Leyendo CSV y convirtiendo a formato columnar (Parquet)...")
    df = pd.read_csv(LOCAL_CSV_PATH)
    df.to_parquet(LOCAL_PARQUET_PATH, engine='pyarrow')
    
    # 3. Conexión a Google Cloud
    print("☁️ Conectando a Google Cloud Storage...")
    # ¡Magia! Aquí Python usa las credenciales que configuraste en la consola
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    
    # 4. Subir el archivo
    blob = bucket.blob(DESTINATION_BLOB_NAME)
    print(f"⬆️ Subiendo archivo a gs://{BUCKET_NAME}/{DESTINATION_BLOB_NAME}...")
    blob.upload_from_filename(LOCAL_PARQUET_PATH)
    
    print("✅ ¡Carga exitosa! El archivo ya está en tu Data Lake.")

if __name__ == '__main__':
    upload_to_gcs()