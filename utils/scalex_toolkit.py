class ScaleXToolkit:
    def output(self, tags_list):
        with open("exports/output.html", "w") as f:
            for tag in tags_list:
                f.write(str(tag))
                f.write('\n\n')

    def unify_word(self, str):
        res = str
        split = False

        if "rice (ro)" in str:
            res = "price"
            split = True
        elif "you pay" in str:
            res = "price"
            split = True

        elif "included minutes" in str:
            res = "flexi_minutes"
            split = True

        elif "included data" in str:
            res = "data_allowance"
            split = True

        elif "valid for" in str:
            res = "duration"
            split = True
        elif "validity" in str:
            res = "duration"
            split = True
        elif "includes" in str:
            res = "data_allowance"
            split = True

        return {"res": res, "split": split}

    def unify_dict(self, dic: dict) -> dict:
        res = {}
        for key, value in dic.items():
            unified_word = self.unify_word(key.lower())
            unified_key = unified_word["res"]
            res[unified_key] = self.split_value_and_unit(
                value) if unified_word["split"] else value
        return res

    def unify_list(self, list):
        res = []
        for dic in list:
            uninfied_dic = self.unify_dict(dic)
            res.append(uninfied_dic)
        return res

    def clear_string(self,  string):  # Removes unwanted characters/texts from string
        texts = ['\n', '\xa0', '/', '#', '*']
        for text in texts:
            string = string.replace(text, '')
        string = string.strip()
        return string

    def split_value_and_unit(self,  string):
        if string == None:
            return
        value = "".join([i for i in string if i.isdigit() or i is '.'])
        unit = "".join([i for i in string if not i.isdigit() and not i is '.'])
        return {"value": value.strip(), "unit": unit.strip()}

    def merge_value_and_unit(self,  dic):
        if dic == "unlimited":
            return "unlimited"
        res = dic["value"] + " " + dic["unit"]
        return self.clear_string(res)

    def merge_plan_value_and_unit(self,  plan: dict):
        new_plan = plan
        try:
            for key, value in new_plan.items():
                if type(value) is dict and "value" in value:
                    new_plan[key] = self.merge_value_and_unit(new_plan[key])
        except:
            pass

        return new_plan

    def best_plan_merge(self,  plan: dict):
        new_plan = plan
        try:
            for key, value in new_plan.items():
                new_plan[key] = self.merge_plan_value_and_unit(
                    new_plan[key])
        except:
            pass

        return new_plan

    def best_plan_list_merge(self,  plans):
        new_plan = []
        try:
            for plan in plans:
                new_plan.append(self.merge_plan_value_and_unit(
                    plan))
        except:
            pass

        return new_plan

    def get_best_plans_from_each_isp(self, all_packages: dict, filter_data) -> dict:
        best_plans = {}
        for isp, isp_packages in all_packages.items():
            for index, package in enumerate(isp_packages):
                if index == 0:
                    clean_plan = package
                    best_plans[isp] = clean_plan
                    clean_plan
                else:

                    clean_plan = self.get_best_package(
                        best_plans[isp], package, filter_data, ['price_value', 'data_allowance_value'])
                    best_plans[isp] = clean_plan
                    clean_plan

        return best_plans

    def get_best_plans(self, all_packages_dic: dict, filter_data) -> dict:

        best_plans = []
        all_packages_list = []
        for isp, isp_packages in all_packages_dic.items():
            all_packages_list += isp_packages
        for main_index in range(0, 6):
            remove_index = 0
            for index, package in enumerate(all_packages_list):
                # if "data_allowance" not in package:
                #     return
                if index == 0:
                    clean_plan = package
                    best_plans.append(clean_plan)
                    remove_index = 0
                else:
                    clean_plan = self.get_best_package(
                        best_plans[main_index], package, filter_data, ['price_value', 'data_allowance_value', "duration_value"])
                    best_plans[main_index] = clean_plan
                    clean_plan
                    remove_index = index
                del all_packages_list[remove_index]

        return best_plans

    def get_best_package(self,  package1: dict, package2: dict, filter_data, fields: list) -> dict:
        best_package = {}
        package1_points = 0
        package2_points = 0
        for field in fields:
            try:
                package1_points += abs(int(package1[field]
                                           ["value"]) - filter_data[field])
                package2_points += abs(int(package2[field]
                                           ["value"]) - filter_data[field])
            except:
                pass

        if package1_points <= package2_points:
            best_package = package1
        else:
            best_package = package2
        return best_package
