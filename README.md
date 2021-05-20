# cli_requests
## Sync/Async CLI Requests

Task requirements:

> write two scripts:
> 1) sync_requests: * script takes as a cli argument a number * using library "requests" * execute a GET the url "https://google.gr" as many times as the number given in step 1 * print the total time of these requests and the total number of times you fetched the url example: python sync_requests.py 20 get 20 sites in x.xx seconds 
> 2) async_requests: * script takes as a cli argument a number * using library "asyncio" and "aiohttp" * execute a GET the url "https://google.gr" as many times as the number given in step 1 * print the total time of these requests and the total number of times you fetched the url example: python async_requests.py 20 get 20 sites in x.xx seconds

> Scripts should be implemented with production grade code. Having security, usability, maintainability and future improvements in mind.


## Use:
> pip install -r requirements.txt
> 
> python3? async_requests.py <amount>
>
> python3? sync_requests.py <amount>