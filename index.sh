mkdir Data
cd Data

for ((i=1;i<=7;i++))
do
dayi='Day'$i

mkdir $dayi
cd $dayi

mkdir Buses
cd Buses

mkdir timestamps
cd timestamps

mkdir BusStops
mkdir Signals
cd ..
echo 'Buses'

cd ..
echo $dayi

cd ..
echo 'Data'
 
done
cd ..
echo 'Original File'
mv '2014-03-01.csv' 'Data/Day1'
mv '2014-03-02.csv' 'Data/Day2'
mv '2014-03-03.csv' 'Data/Day3'
mv '2014-03-04.csv' 'Data/Day5'
mv '2014-03-05.csv' 'Data/Day6'
mv '2014-03-07.csv' 'Data/Day7'

python View_data.py
python mapping.py
python Long_Lat_Time.py
#python clustering.py


