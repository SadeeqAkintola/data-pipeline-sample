import datetime
 
from airflow import models
from airflow.operators import BashOperator
 
 
yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())
 
 
default_args = {
	'start_date':yesterday
}
 
with models.DAG(
	'load-stocks-airflow-job-bash',
	schedule_interval=None,
	default_args=default_args) as dag:
        bash_command = """
        export GOOGLE_APPLICATION_CREDENTIALS=/home/datatalkswithsadeeq/stocks-project/stocks-project-2-a3ae1bfbbf92.json
        python /home/datatalkswithsadeeq/stocks-project/load-stocks.py --runner=DataflowRunner --output=gs://"staging-bucket"/out --temp_location=gs://"staging-bucket"/teemp --staging_location=gs://"staging-bucket"/staging --project=stocks-project-2
        """
 
bash_run_job = BashOperator(task_id='run_job_from_bash_command', bash_command=bash_command)
       
bash_run_job