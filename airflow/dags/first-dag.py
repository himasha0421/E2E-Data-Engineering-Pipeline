from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {"owner": "Himasha", "retries": 5, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="first_dag",
    description="This is our first example dag",
    start_date=datetime(2024, 1, 15, 23),
    schedule_interval="@daily",
    default_args=default_args,
) as dag:
    first_task = BashOperator(
        task_id="first-task",
        bash_command="echo Hello World !",
    )

    second_task = BashOperator(
        task_id="second-task",
        bash_command="echo this is the second task , execute after task 1",
    )

    third_task = BashOperator(
        task_id="third-task",
        bash_command="echo this is task 3 , run after task 1 , parallely with task 2",
    )
    # apply task dependencies method 1
    first_task.set_downstream(second_task)
    first_task.set_downstream(third_task)

    # method 2
    # first_task >> second_task
    # first_task >> third_task

    # method 3
    # first_task >> [second_task,third_task]
