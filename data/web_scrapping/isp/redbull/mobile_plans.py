from data.web_scrapping.isp.redbull.redbull_toolkit import RedbullToolkit


class RedbullMobilePlans(RedbullToolkit):

    def __init__(self) -> None:
        super().__init__()
        self.packages = []
        self.soup = self.get_soup(self.MOBILE_PLANS_URL)
        self.get_packages()

    def get_packages(self):
        package_blocks = self.soup.select("div.home__card-inner")

        for block in package_blocks:
            package = {}
            price = block.select_one(
                "div.home__card-title").text
            duration = block.select_one("div.home__card-date").text
            all_net_minutes = block.select_one("div.home__card-bonus").text
            included_data = block.select_one("div.home__card-capacity").text
            package["price"] = self.split_value_and_unit(price)
            package["data_allowance"] = self.split_value_and_unit(
                included_data)
            package["all_net_minutes"] = self.split_value_and_unit(
                all_net_minutes)
            package["duration"] = self.split_value_and_unit(duration)
            package["isp"] = "redbull"
            self.packages.append(package)
