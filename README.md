# DataPoint Client

A wrapper around the [Met Office Datapoint Client API](https://www.metoffice.gov.uk/services/data/datapoint).

## Setup the client

To use this client, you will need a [DataPoint API key](https://www.metoffice.gov.uk/services/data/datapoint/api).

Install from GitHub using Pip.

Import the client:
```py
from datapoint_client.client import DatapointClient
```

Initialize it with the DataPoint API key:
```py
client = DatapointClient(datapoint_api_key)
```

## Get data
Find the ID of the site you want data for using the DataPoint documentation.

Then get observations for that site:

```py
client.get_obs_for_site(site_id)
```

Or the three hourly forecasts for the site:

```py
client.get_3hourly_forecasts_for_site(site_id)
```
