import datetime
 
from airflow import models
from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator
from airflow.operators import BashOperator
yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())
 
 
default_args = {
    'start_date':yesterday
}
 
with models.DAG(
    'dataflow_python_dag',
    schedule_interval=None,
    default_args=default_args) as dag:
    
    bash_nothing = BashOperator(task_id='nothing_2',bash_command='echo nothing')
    
    run_dataflow_python = DataFlowPythonOperator(
		    task_id='dataflow_python_task',
		    py_file='/home/datatalkswithsadeeq/stocks-project/wordcount.py',
		    options={'runner':'DataflowRunner',
			     'output':'gs://stocks-project-2/out1',
			     'temp_location':'gs://stocks-project-2/temp1',
			     'staging_location':'gs://stocks-project-2/staging1',
			     'project':'stocks-project-2'},
		    gcp_conn_id='cloud-dataflow-hijo-project-from-location')
    bash_nothing >> run_dataflow_python