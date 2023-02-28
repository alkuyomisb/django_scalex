# from scalex.isp.omantel.heyyak_plus import OmantelHeyyakPlus
# from scalex.isp.omantel.baqati import OmantelBaqati
# from scalex.isp.ooredoo.shahry import OoredooShahry
# from scalex.isp.omantel.tourist_packs import TouristPacks
# from scalex.isp.awaser.fiber_home import FiberHome
# from scalex.isp.ooredoo.hala import OoredooHala
# from scalex.scalex_toolkit import ScaleXToolkit
# from scalex.isp.redbull.mobile_plans import MobilePlans
# from scalex.isp.rennah.rennah_mobile import RennahMobile


class ScaleXToolkit:
    def output(self, tags_list):
        with open("output.html", "w") as f:
            for tag in tags_list:
                f.write(str(tag))
                f.write('\n\n')

    def clear_string(self,  string):  # Removes unwanted characters/texts from string
        texts = ['\n', '\xa0', '/']
        for text in texts:
            string = string.replace(text, '')
        string = string.strip()
        return string

    def split_value_and_unit(self,  string):
        if string == None:
            return
        value = "".join([i for i in string if i.isdigit()])
        unit = "".join([i for i in string if not i.isdigit()])
        return {"value": value.strip(), "unit": unit.strip()}

    def merge_value_and_unit(self,  dic):
        if dic == "unlimited":
            return "unlimited"
        return dic["value"] + " " + dic["unit"]

    def get_best_plans(self, OTPackages, filter_data) -> dict:
        best_plans = {}
        # heyyak_plus = OmantelHeyyakPlus()
        # baqati = OmantelBaqati()
        # fiber_home = FiberHome()
        # tourist_packs = TouristPacks()
        # mobile_plans = MobilePlans()
        # rennah_mobile = RennahMobile()
        for index, package in enumerate(OTPackages):
            if index == 0:
                best_plans["omantel"] = package
            else:
                best_plans["omantel"] = self.get_best_package(
                    best_plans["omantel"], package, filter_data, ['price', 'data_allowance'])

        return best_plans

    def get_best_package(self,  package1: dict, package2: dict, filter_data, fields: list) -> dict:
        best_package = {}
        package1_points = 0
        package2_points = 0
        for field in fields:
            try:
                package1_points += abs(float(package1[field]
                                             ["value"]) - filter_data[field])
                package2_points += abs(float(package2[field]
                                             ["value"]) - filter_data[field])
            except:
                pass
        if package1_points <= package2_points:
            best_package = package1
        else:
            best_package = package2
        return best_package
