{{ config(materialized='table') }}

WITH raw_orders AS (
    SELECT * 
    FROM {{ source('ecommerce_raw', 'orders') }}
),

cleaned_orders AS (
    SELECT 
        order_id,
        customer_id,
        order_status,
        -- Convertimos el texto a formato de Fecha/Hora real
        CAST(order_purchase_timestamp AS TIMESTAMP) AS purchase_date,
        -- Convertimos a fecha estimada de entrega
        CAST(order_estimated_delivery_date AS TIMESTAMP) AS estimated_delivery_date
    FROM raw_orders
    -- A Power BI solo le importan los pedidos que sí se entregaron
    WHERE order_status = 'delivered'
)

SELECT * FROM cleaned_orders