from google.cloud import bigquery

# 1. Configuraciones
# ¡Cambia esto por el ID de tu proyecto que sale en la consola de Google Cloud!
PROJECT_ID = 'project-59fdbdb5-71ea-4b99-835' 
DATASET_ID = 'ecommerce_raw'
TABLE_ID = 'orders'

# La ruta exacta de tu archivo en el Data Lake
GCS_URI = 'gs://brayan-data-lake-olist/raw/orders/olist_orders.parquet'

def load_parquet_to_bq():
    print("🚀 Iniciando carga desde Data Lake hacia Data Warehouse...")
    
    # Iniciar cliente de BigQuery
    client = bigquery.Client(project=PROJECT_ID)
    
    # Configurar el trabajo de carga (Load Job)
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE, # Si la tabla existe, la reemplaza
    )
    
    print(f"📦 Leyendo archivo desde {GCS_URI}...")
    # Ejecutar el trabajo
    load_job = client.load_table_from_uri(
        GCS_URI,
        table_ref,
        job_config=job_config
    )
    
    # Esperar a que termine
    load_job.result()
    
    # Validar cuántas filas se cargaron
    table = client.get_table(table_ref)
    print(f"✅ ¡Éxito! La tabla {TABLE_ID} ahora tiene {table.num_rows} filas en BigQuery.")

if __name__ == '__main__':
    load_parquet_to_bq()