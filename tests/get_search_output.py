import requests
import json
import logging
import sys
import json
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.config import headers, base_url, cache_dir
from src.tools.logger import setup_logger

# logger = setup_logger()
url = base_url

# GraphQL запрос для получения списка объявлений
query = """
query ListingSearchQuery($searchParameters: [SearchParameter!] = {key: "", value: ""}) {
  clientCompatibleListings(searchParameters: $searchParameters) {
    __typename
    ... on ListingSuccess {
      __typename
      data {
        id
        location {
          city {
            id
            name
            normalized_name
            _nodeId
          }
          district {
            id
            name
            normalized_name
            _nodeId
          }
          region {
            id
            name
            normalized_name
            _nodeId
          }
        }
        last_refresh_time
        delivery {
          rock {
            active
            mode
            offer_id
          }
        }
        created_time
        category {
          id
          type
          _nodeId
        }
        contact {
          courier
          chat
          name
          negotiation
          phone
        }
        business
        omnibus_pushup_time
        photos {
          link
          height
          rotation
          width
        }
        promotion {
          highlighted
          top_ad
          options
          premium_ad_page
          urgent
          b2c_ad_page
        }
        protect_phone
        shop {
          subdomain
        }
        title
        status
        url
        user {
          id
          uuid
          _nodeId
          about
          b2c_business_page
          banner_desktop
          banner_mobile
          company_name
          created
          is_online
          last_seen
          logo
          logo_ad_page
          name
          other_ads_enabled
          photo
          seller_type
          social_network_account_type
        }
        offer_type
        params {
          key
          name
          type
          value {
            __typename
            ... on GenericParam {
              key
              label
            }
            ... on CheckboxesParam {
              label
              checkboxParamKey: key
            }
            ... on PriceParam {
              value
              type
              previous_value
              previous_label
              negotiable
              label
              currency
              converted_value
              converted_previous_value
              converted_currency
              arranged
              budget
            }
            ... on SalaryParam {
              from
              to
              arranged
              converted_currency
              converted_from
              converted_to
              currency
              gross
              type
            }
            ... on ErrorParam {
              message
            }
          }
        }
        _nodeId
        description
        external_url
        key_params
        partner {
          code
        }
        map {
          lat
          lon
          radius
          show_detailed
          zoom
        }
        safedeal {
          allowed_quantity
          weight_grams
        }
        valid_to_time
      }
      metadata {
        filter_suggestions {
          category
          label
          name
          type
          unit
          values {
            label
            value
          }
          constraints {
            type
          }
          search_label
          option {
            ranges
            order
            orderForSearch
            fakeCategory
          }
        }
        x_request_id
        search_id
        total_elements
        visible_total_count
        source
        search_suggestion {
          url
          type
          changes {
            category_id
            city_id
            distance
            district_id
            query
            region_id
            strategy
            excluded_category_id
          }
        }
        facets {
          category {
            id
            count
            label
            url
          }
          category_id_1 {
            count
            id
            label
            url
          }
          category_id_2 {
            count
            id
            label
            url
          }
          category_without_exclusions {
            count
            id
            label
            url
          }
          category_id_3_without_exclusions {
            id
            count
            label
            url
          }
          city {
            count
            id
            label
            url
          }
          district {
            count
            id
            label
            url
          }
          owner_type {
            count
            id
            label
            url
          }
          region {
            id
            count
            label
            url
          }
          scope {
            id
            count
            label
            url
          }
        }
        new
        promoted
      }
      links {
        first {
          href
        }
        next {
          href
        }
        previous {
          href
        }
        self {
          href
        }
      }
    }
    ... on ListingError {
      __typename
      error {
        code
        detail
        status
        title
        validation {
          detail
          field
          title
        }
      }
    }
  }
}
"""

payload = json.dumps({
  "query": query,
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

response = requests.request("POST", url, headers=headers, data=payload)

# logger.info(response.text)
with open(f"{cache_dir}/search_output.json", "w", encoding="utf-8") as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)