# General imports to be used in the views
from django.shortcuts import render
from django.http import JsonResponse

from views.statistics import statistics
from views.tab import tab
from views.data import data
from views.plans import plans
from views.index import index
from views.filter import filter
from views.result import result
from domain.scalex_toolkit import ScaleXToolkit


# Import all the views so that we can access them from one file
