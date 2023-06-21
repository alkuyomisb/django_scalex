import mysql.connector

def get_all_plans ():
    plans = []
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM plan")
    myresult = mycursor.fetchall()

    for plan in myresult:
        p = record_to_dict(plan)
        plans.append(p)
    

   
    mydb.close()
    return plans

def display_columns_names ():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    cursor = mydb.cursor()
    query = f"SHOW COLUMNS FROM plan"
    cursor.execute(query)

    column_names = [column[0] for column in cursor.fetchall()]
 
    cursor.close()
    mydb.close()
    return column_names



def get_plans(**conditions):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    query_conditions = ""

    for index, condition in enumerate(conditions):
        if conditions[condition] == "all":
            continue

        if index != 0:
            query_conditions += " AND "
        else:
            query_conditions += " WHERE "

        query_conditions += "{} = '{}'".format(
            condition, conditions[condition])

    query = "SELECT * FROM plan {} ;".format(query_conditions)
    print(query)
    cursor = db.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    plans = []
    

    for index, record in enumerate(records):
        data = {
            "price_value": record[1],
            "price_unit": record[2],
            "data_allowance_value": record[3],
            "data_allowance_unit": record[4],
            "flexi_minutes": record[5],
            "local_minutes": record[6],
            "international_minutes": record[7],
            "duration_value": record[8],
            "duration_unit": record[9],
            "isp": record[10],
            "link": record[11],
            "social_media_data_value": record[12],
            "social_media_data_unit": record[13],
            "last_checked ": record[14],
            "status": record[15],
            "service_type": record[16],
            "plan_type": record[17],
            "title": record[18],
            "sms": record[19],
            "download_speed_value": record[20],
            "download_speed_unit": record[21],
            "upload_speed_value": record[22],
            "upload_speed_unit": record[23],
            "fixed_line_minutes": record[24],
            "world_roaming_value": record[25],
            "world_roaming_unit": record[26],
            "contract_duration_value": record[27],
            "contract_duration_unit": record[28],
            "add_on_link": record[29]
        }
        plans.append(data)
    db.close()
    return plans


def get_one_closest(filter_dict, orders_by_dict, limit):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    # Conditions
    query_conditions = ""
    for index, condition in enumerate(filter_dict):
        if filter_dict[condition] == "all":
            continue

        if index != 0:
            query_conditions += " AND "
        else:
            query_conditions += " WHERE "

        query_conditions += "{} = '{}'".format(
            condition, filter_dict[condition])

    # Order By
    query_orders_by = ""
    query_distances = ""
    for index, order_by in enumerate(orders_by_dict):
        query_distances += " , abs({} - {}) as distance_from_{} ".format(
            order_by, orders_by_dict[order_by], order_by)
        if index != 0:
            query_orders_by += " , distance_from_{} ".format(order_by)
        else:
            query_orders_by += "distance_from_{} ".format(order_by)

    query = """
            SELECT   *
            {}
            FROM  plan
            {}
            ORDER BY {}
            LIMIT 0,{}
            """.format(query_distances, query_conditions, query_orders_by, limit)

    cursor = db.cursor()
    cursor.execute(query)
    if limit == 1:
        record = cursor.fetchone()
        if cursor.rowcount == 0:
            return get_empty_dict()
        data = record_to_dict(record)
        db.close()
        return data
    else:
        records = cursor.fetchall()
        data_list = []
        print(data_list)
        print("______________________________________________________________________")

        for record in records:
            data = record_to_dict(record)
            # print(data)
            data_list.append(data)
            print(data_list)
            print("TYPE: " + str(type(data_list)))
            print(
                "______________________________________________________________________")

        db.close()
        return data_list


def record_to_dict(record):
    data = {
        "price_value": record[1],
        "price_unit": record[2],
        "data_allowance_value": record[3],
        "data_allowance_unit": record[4],
        "flexi_minutes": record[5],
        "local_minutes": record[6],
        "international_minutes": record[7],
        "duration_value": record[8],
        "duration_unit": record[9],
        "isp": record[10],
        "link": record[11],
        "social_media_data_value": record[12],
        "social_media_data_unit": record[13],
        "last_checked ": record[14],
        "status": record[15],
        "service_type": record[16],
        "plan_type": record[17],
        "title": record[18],
        "sms": record[19],
        "download_speed_value": record[20],
        "download_speed_unit": record[21],
        "upload_speed_value": record[22],
        "upload_speed_unit": record[23],
        "fixed_line_minutes": record[24],
        "world_roaming_value": record[25],
        "world_roaming_unit": record[26],
        "contract_duration_value": record[27],
        "contract_duration_unit": record[28],
        "add_on_link": record[29]
    }
    return data


def get_empty_dict():
    data = {
        "price_value": "-",
        "price_unit": "-",
        "data_allowance_value": "-",
        "data_allowance_unit": "-",
        "flexi_minutes": "-",
        "local_minutes": "-",
        "international_minutes": "-",
        "duration_value": "-",
        "duration_unit": "-",
        "isp": "-",
        "link": "-",
        "social_media_data_value": "-",
        "social_media_data_unit": "-",
        "last_checked ": "-",
        "status": "-",
        "service_type": "-",
        "plan_type": "-",
        "title": "-",
        "sms": "-",
        "download_speed_value": "-",
        "download_speed_unit": "-",
        "upload_speed_value": "-",
        "upload_speed_unit": "-",
        "fixed_line_minutes": "-",
        "world_roaming_value": "-",
        "world_roaming_unit": "-",
        "contract_duration_value": "-",
        "contract_duration_unit": "-",
        "add_on_link": "-"
    }
    return data

def add_chart(chartType ,plan_fields):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    cursor = db.cursor()
    cursor.execute("INSERT INTO charts (chart_type) values ('{}' );".format(chartType ))
    chart_id = cursor.lastrowid  
    print("chart id: ",chart_id);
    for plan_field in plan_fields:
        cursor.execute("INSERT INTO chart_parameters (chart_id , plan_field) VALUES ('{}','{}')".format(chart_id , plan_field))

    db.commit()
    cursor.close()
    db.close()


def delete_chart_and_parameters(chart_id):
    try:
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
        )
        cursor = db.cursor()

        # Delete the chart from the charts table
        delete_chart_query = "DELETE FROM charts WHERE id = %s"
        cursor.execute(delete_chart_query, (chart_id,))

        # Delete the chart parameters from the chart_parameters table
        delete_params_query = "DELETE FROM chart_parameters WHERE chart_id = %s"
        cursor.execute(delete_params_query, (chart_id,))

        db.commit()
        cursor.close()
        db.close()

        print("Chart and associated parameters deleted successfully.")
    except mysql.connector.Error as error:
        print("Error deleting chart and associated parameters:", error)
        
        


def get_charts ():
    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )
    cursor = db.cursor()

    chart_query = "SELECT chart_type , id FROM charts"  #retreive all charts
    cursor.execute(chart_query)
    chart_results = cursor.fetchall()
    #store the data
    data = {"charts": []}

    # display chart type 
    for chart_row in chart_results: 
        chart_type = chart_row[0] #store chart_type
        chart_id = chart_row[1]
        if chart_type == 'pie': #check chart type

            # Retrieve parameters for the specific chart type from the chart_parameters table
            param_query = """
            SELECT plan_field
            FROM chart_parameters
            WHERE chart_id = %s;
            """
            cursor.execute(param_query, (chart_id,))
            param_results = cursor.fetchall()

            #chart dictionary
            chart = {
                "id" : chart_id,
                "chartType": chart_type,
                "parameters": []
            }
            

            # display the parameters and value for the specific chart type
            for param_row in param_results:
                parameter = {
                "plan_field": param_row[0],
                "value": None,
                }


                # get the sum of plan field from plan table 
                sum_query = "SELECT SUM(CAST({} AS DECIMAL)) FROM plan".format(param_row[0])
                cursor.execute(sum_query)
                sum_result = cursor.fetchone()
                parameter["value"] = int(sum_result[0])
                chart["parameters"].append(parameter)

            # data["charts"].append(chart)

                     
        elif chart_type in ['line', 'bar']: #check anothe chart type

            # Retrieve parameters for the specific chart type from the chart_parameters table
            param_query = """
            SELECT plan_field
            FROM chart_parameters
            WHERE chart_id = %s;
            """
            cursor.execute(param_query, (chart_id,))
            param_results = cursor.fetchall()

            #chart dictionary
            chart = {
                "id" : chart_id , 
                "chartType": chart_type,
                "lables": [],
                "values" : []
            }
            

            # display the parameters and value for the specific chart type
            for param_row in param_results:
                chart["lables"].append(
                    param_row[0],
                )
            x = param_results[0][0]
            y = param_results[1][0]
            chart_values = retrieve_xy_values(x, y)
            chart["values"] = chart_values
            
        data["charts"].append(chart)
            



    cursor.close()
    db.close()
    return data


def retrieve_xy_values(column1_name, column2_name):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )
    cursor = db.cursor()
    query = "SELECT {0}, {1} FROM plan".format(column1_name, column2_name)
    cursor.execute(query)

    values = cursor.fetchall()
    cursor.close()
    db.close()

    chart_values = []
    for value in values:
        if len(value) >= 2 and all(is_numeric(val) for val in value):
            x_value = float(str(value[0]))
            y_value = float(str(value[1]))
            chart_values.append({"x": x_value, "y": y_value})
            
    return chart_values



def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False




    














    
    
    
   
