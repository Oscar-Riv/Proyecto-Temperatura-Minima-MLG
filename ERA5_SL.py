import cdsapi

c = cdsapi.Client()


#------------------------------------------
#Ruta de guardado
path = '/exports/home/odriverar/ERA5/'

#Variables ERA5
#varname =['2m_temperature',
#          '2m_dewpoint_temperature',
#          'minimum_2m_temperature_since_previous_post_processing', 
#          '10m_u_component_of_wind', 
#          '10m_v_component_of_wind',
#          'surface_net_thermal_radiation',
#          'total_precipitation',
#          'surface_pressure',
#          'total_cloud_cover',
#          'boundary_layer_height','total_column_water_vapour',
#          'total_column_water_vapour',
#          'low_cloud_cover']

varname =['geopotential']

#Variables guardado
#savename=['T2M','T2R','T2MIN','U','V','SNR','PPT','PA','TCC','BLY','TCWP','LCC']
savename=['GEO']

#Años e intervalos
YR_int = [['1981', '1982', '1983','1984', '1985', '1986','1987', '1988', '1989','1990', '1991'],
          ['1992', '1993', '1994','1995', '1996', '1997','1998', '1999', '2000','2001', '2002'],
          ['2003', '2004', '2005','2006', '2007', '2008','2009', '2010', '2011','2012', '2013'],
          ['2014', '2015', '2016','2017', '2018', '2019','2020', '2021']]

#Años e intervalos para guardado de archivos
inter = ['_1981-1991','_1992-2002','_2003-2013','_2014-2021']

#Meses
month = ['01', '02', '03','04', '05', '06','07', '08', '09','10', '11', '12',]

#Dias
days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16',
        '17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

#Horas
hour = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00',
        '12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']

#Coordenadas area N,W,S,E 
area = [13, -80, -5, -66]

#Loop de descarga y guardado de datos
for i in range (len(varname)):
    for j in range (len(YR_int)):
        name = savename[i]+inter[j]+'.nc'
        c.retrieve(
	    'reanalysis-era5-single-levels',
	    {
		'variable':varname[i],
		'product_type':'reanalysis',
		'area':area,		#N/W/S/E
		'year':YR_int[j],
		'month':month[:],
		'day':days[:],
		'time':hour[:],
		'format':'netcdf'
	    },
	    path+name)
