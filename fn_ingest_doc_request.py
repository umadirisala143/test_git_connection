import os
import requests


def fn_ingest_doc_request(config=None, **req):
    resume_pdf_path = "minio://ensolive/testuiautomation_ef223ac4-2602-425a-8bc0-d117369e33bb/console/direct/2084d841-3d9f-4a08-9386-4720298b2805/test_resume1.pdf"
    ingest_req =  { "file_path": [ resume_pdf_path ] }
    return ingest_req


