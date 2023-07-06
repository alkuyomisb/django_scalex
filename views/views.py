# General imports to be used in the views
from django.shortcuts import render
from django.http import JsonResponse

from views.login import login
from views.statistics import statistics
from views.tab import tab
from views.plans import plans
from views.index import index
from views.result import result
from views.save_chart import save_chart
from views.delete_chart import delete_chart
# from views.export_data import export_data
from views.export_filter_data import export_filter_data
from utils.scalex_toolkit import ScaleXToolkit
