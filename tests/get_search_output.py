import requests
import json

url = "https://www.olx.ua/apigateway/graphql"

payload = json.dumps({
  "query": "query ListingSearchQuery(\n  $searchParameters: [SearchParameter!] = {key: \"\", value: \"\"}\n) {\n  clientCompatibleListings(searchParameters: $searchParameters) {\n    __typename\n    ... on ListingSuccess {\n      __typename\n      data {\n        id\n        location {\n          city {\n            id\n            name\n            normalized_name\n            _nodeId\n          }\n          district {\n            id\n            name\n            normalized_name\n            _nodeId\n          }\n          region {\n            id\n            name\n            normalized_name\n            _nodeId\n          }\n        }\n        last_refresh_time\n        delivery {\n          rock {\n            active\n            mode\n            offer_id\n          }\n        }\n        created_time\n        category {\n          id\n          type\n          _nodeId\n        }\n        contact {\n          courier\n          chat\n          name\n          negotiation\n          phone\n        }\n        business\n        omnibus_pushup_time\n        photos {\n          link\n          height\n          rotation\n          width\n        }\n        promotion {\n          highlighted\n          top_ad\n          options\n          premium_ad_page\n          urgent\n          b2c_ad_page\n        }\n        protect_phone\n        shop {\n          subdomain\n        }\n        title\n        status\n        url\n        user {\n          id\n          uuid\n          _nodeId\n          about\n          b2c_business_page\n          banner_desktop\n          banner_mobile\n          company_name\n          created\n          is_online\n          last_seen\n          logo\n          logo_ad_page\n          name\n          other_ads_enabled\n          photo\n          seller_type\n          social_network_account_type\n        }\n        offer_type\n        params {\n          key\n          name\n          type\n          value {\n            __typename\n            ... on GenericParam {\n              key\n              label\n            }\n            ... on CheckboxesParam {\n              label\n              checkboxParamKey: key\n            }\n            ... on PriceParam {\n              value\n              type\n              previous_value\n              previous_label\n              negotiable\n              label\n              currency\n              converted_value\n              converted_previous_value\n              converted_currency\n              arranged\n              budget\n            }\n            ... on SalaryParam {\n              from\n              to\n              arranged\n              converted_currency\n              converted_from\n              converted_to\n              currency\n              gross\n              type\n            }\n            ... on ErrorParam {\n              message\n            }\n          }\n        }\n        _nodeId\n        description\n        external_url\n        key_params\n        partner {\n          code\n        }\n        map {\n          lat\n          lon\n          radius\n          show_detailed\n          zoom\n        }\n        safedeal {\n          allowed_quantity\n          weight_grams\n        }\n        valid_to_time\n      }\n      metadata {\n        filter_suggestions {\n          category\n          label\n          name\n          type\n          unit\n          values {\n            label\n            value\n          }\n          constraints {\n            type\n          }\n          search_label\n          option {\n            ranges\n            order\n            orderForSearch\n            fakeCategory\n          }\n        }\n        x_request_id\n        search_id\n        total_elements\n        visible_total_count\n        source\n        search_suggestion {\n          url\n          type\n          changes {\n            category_id\n            city_id\n            distance\n            district_id\n            query\n            region_id\n            strategy\n            excluded_category_id\n          }\n        }\n        facets {\n          category {\n            id\n            count\n            label\n            url\n          }\n          category_id_1 {\n            count\n            id\n            label\n            url\n          }\n          category_id_2 {\n            count\n            id\n            label\n            url\n          }\n          category_without_exclusions {\n            count\n            id\n            label\n            url\n          }\n          category_id_3_without_exclusions {\n            id\n            count\n            label\n            url\n          }\n          city {\n            count\n            id\n            label\n            url\n          }\n          district {\n            count\n            id\n            label\n            url\n          }\n          owner_type {\n            count\n            id\n            label\n            url\n          }\n          region {\n            id\n            count\n            label\n            url\n          }\n          scope {\n            id\n            count\n            label\n            url\n          }\n        }\n        new\n        promoted\n      }\n      links {\n        first {\n          href\n        }\n        next {\n          href\n        }\n        previous {\n          href\n        }\n        self {\n          href\n        }\n      }\n    }\n    ... on ListingError {\n      __typename\n      error {\n        code\n        detail\n        status\n        title\n        validation {\n          detail\n          field\n          title\n        }\n      }\n    }\n  }\n}\n",
  "variables": {
    "searchParameters": [
      {
        "key": "offset",
        "value": "0"
      },
      {
        "key": "limit",
        "value": "40"
      },
      {
        "key": "query",
        "value": "квартира оренда"
      },
      {
        "key": "category_id",
        "value": "1760"
      },
      {
        "key": "region_id",
        "value": "21"
      },
      {
        "key": "city_id",
        "value": "121"
      },
      {
        "key": "owner_type",
        "value": "private"
      },
      {
        "key": "currency",
        "value": "UAH"
      },
      {
        "key": "sort_by",
        "value": "created_at:desc"
      },
      {
        "key": "filter_enum_furnish[0]",
        "value": "yes"
      },
      {
        "key": "filter_enum_number_of_rooms_string[0]",
        "value": "dvuhkomnatnye"
      },
      {
        "key": "filter_enum_number_of_rooms_string[1]",
        "value": "odnokomnatnye"
      },
      {
        "key": "filter_float_floor:from",
        "value": "2"
      },
      {
        "key": "filter_float_price:from",
        "value": "10000"
      },
      {
        "key": "filter_float_price:to",
        "value": "15000"
      },
      {
        "key": "filter_float_total_area:from",
        "value": "30"
      },
      {
        "key": "filter_float_total_area:to",
        "value": "60"
      },
      {
        "key": "filter_float_total_floors:from",
        "value": "2"
      },
      {
        "key": "filter_refiners",
        "value": "spell_checker"
      },
      {
        "key": "suggest_filters",
        "value": "true"
      },
      {
        "key": "sl",
        "value": "19a5ae6ea4ax405202ee"
      }
    ]
  }
})
headers = {
  'Cookie': 'PHPSESSID=p27bgldl1phjn3oa1a7dn7fsji',
  'Content-Type': 'application/json',
  'accept-language': 'uk',
  'authorization': 'Bearer eyJraWQiOiI3TzI5clpiaDVHXC9SR3NTZ2g2ZzZRN1QrMVJZdTdsWFwvXC9qd3dyWnozVjNzPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIyMGZkNDljNi1hZDBiLTRiMjItOGYzZC05NWUyYjZmYjI2OTgiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtd2VzdC0xLmFtYXpvbmF3cy5jb21cL2V1LXdlc3QtMV9WMkFKVVgwWEUiLCJjbGllbnRfaWQiOiIzMDlsc2doMGRlaXJsbzJsYTlrbXJtaGUzdiIsIm9yaWdpbl9qdGkiOiJjYzBkNzM4ZC03NDZkLTQyOWYtYTg3ZC01YTlhNWRhMGJmMDAiLCJldmVudF9pZCI6IjE0YTU2MjA3LWVhYmMtNGRjYy1hNDRiLWNhMGY2ZDU3YmM1NCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3NjI2MzcxNzUsImV4cCI6MTc2MjYzODk1NSwiaWF0IjoxNzYyNjM4MDU1LCJqdGkiOiJkMWFlNDJmYy0zZjk3LTQ1NDYtYmM3NS00NmI5YWU0OTZkZWYiLCJ1c2VybmFtZSI6IjU1NTljMDU5LWMyYzItNDUzMS04MzQxLWEwZGNhNjI1ZDRlNyJ9.PRL5aOyPN1w-9DDmLidXegulTHCQ5YeHki0wf2TEtxn41ZPcnXR6szZIg05cuoFEHcIBqAlEQ6KLKbEnhWCx5s8uPdl-p6HkS-i1-BUXPqjhJ7fg5C7aInCryI8qqqc1PIrB0Qz1TN2gIonvr3yHi2jsZTtj-4U_tO-WFu-PzVJT0wRK7fmRpyBLsAPicC6nqeqz0a2TwYlWtD5ErMiMv3ePIz_NqPyqwN1aT-sHJqwQZss3j1F3NZSAk7J_tTQtS2ii-r-ZXPmW1nFYZ8vF-s507AVo50twfmdIeV0Mm3y7Tvy93Ht_kI8h5RZBTrywcSitih689v3C8xqtqIfuXw',
  'content-type': 'application/json',
  'origin': 'https://www.olx.ua',
  'priority': 'u=1, i',
  'referer': 'https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/dnepr/q-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%B0-%D0%BE%D1%80%D0%B5%D0%BD%D0%B4%D0%B0/?currency=UAH&search%5Bprivate_business%5D=private&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=10000&search%5Bfilter_float_price:to%5D=15000&search%5Bfilter_float_floor:from%5D=2&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_float_total_area:from%5D=30&search%5Bfilter_float_total_area:to%5D=60&search%5Bfilter_enum_furnish%5D%5B0%5D=yes&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=dvuhkomnatnye&search%5Bfilter_enum_number_of_rooms_string%5D%5B1%5D=odnokomnatnye',
  'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'x-client': 'DESKTOP'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
with open
