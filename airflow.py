# -*- coding: utf-8 -*-
"""Airflow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I5AdTNu0Nw8P4A0Kpd7qqwAc4TyIMaID
"""

# ! pip install apache-airflow

from airflow import DAG
from airflow.utils.dates import days_ago

from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from airflow.utils.helpers import chain, cross_downstream
from random import seed, random
from datetime import timedelta

default_arguments = {
    "owner" : "aman kumar",
    "start_date" : days_ago(1)
}

with DAG("core_concepts", schedule_interval="@daily", catchup=False, default_args=default_arguments) as dag:

  bash_task = BashOperator(task_id= "bash_command", bash_command="echo $TODAY", env={"Today": "2020-05-21"})

  def print_random_number(number):
    seed(number)
    print(random())

  python_task = PythonOperator(
      task_id = "python_function",
      python_function = print_random_number,
      op_args = [1]
      
  )  

bash_task >> python_task