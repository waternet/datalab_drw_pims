# datalab_drw_pims
PIMS data wrapper

### voorbeelden van beschikbare functies 
Hieronder enkele voorbeelden van het gebruik van de python wrapper.

#### Current value
```python
import wnpims

api = wnpims.API()
dataframe = api.get_curr_val("VVZ1GA01GM00__VD")
```

#### Trend
```python
import wnpims

api = wnpims.API()
start = datetime.datetime(2015,1,1)
end = datetime.datetime(2015,12,31)
dataframe = api.get_trend(tagname='VVZ1GA01GM001_VD', alist='GAS-DW-VD', start=start, end=end)
```

#### Trend Pivot
```python
import wnpims

api = wnpims.API()
start = datetime.datetime(2015,1,1)
end = datetime.datetime(2015,12,31)
dataframe = api.get_trend_pivot(tagname='VVZ1GA01GM001_VD', alist='GAS-DW-VD', start=start, end=end)
```
