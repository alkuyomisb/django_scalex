# General imports to be used in the views
from django.shortcuts import render
from django.http import JsonResponse

from views.statistics import statistics
from views.tab import tab
from views.plans import plans
from views.index import index
from views.result import result
# from views.export_data import export_data
from views.export_filter_data import export_filter_data
from utils.scalex_toolkit import ScaleXToolkit


# Import all the views so that we can access them from one file
