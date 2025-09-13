from cianparser import CianParser


parser = CianParser(location="Новосибирск")

data = parser.get_flats(
    deal_type="rent_long",
    rooms="all",
    with_saving_csv=True,
    with_extra_data=False,
    additional_settings={"start_page":1, "end_page":1},
)