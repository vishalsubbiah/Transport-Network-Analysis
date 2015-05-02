mkdir -p 'Data'
cd 'Data'
for i in 1 2 3 4 5 6 7
do
	mkdir -p 'Day'$i
	echo 'Day'$i
	cd 'Day'$i
	mkdir -p 'Buses'
	cd 'Buses'
	mkdir -p 'timestamps'
	cd 'timestamps'
	mkdir -p 'BusStops'
	mkdir -p 'Signals'
	cd ..
	echo 'Buses'
	cd ..
	echo $dayi
	cd ..
	echo 'Data'
done
cd ..
echo 'Original File'
cp '2014-03-01.csv' 'Data/Day1'
cp '2014-03-02.csv' 'Data/Day2'
cp '2014-03-03.csv' 'Data/Day3'
cp '2014-03-04.csv' 'Data/Day4'
cp '2014-03-05.csv' 'Data/Day5'
cp '2014-03-06.csv' 'Data/Day6'
cp '2014-03-07.csv' 'Data/Day7'
python View_data.py
python mapping.py
python Long_Lat_Time.py
python clustering.py


