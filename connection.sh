#!/bin/bash

dir="/opt/dionaea/var/log/dionaea"

#dump du nb de ligne
new=`grep -c "accepted connection" $dir/dionaea.log`

#prend une valeur du nombre de ligne
last=`cat /tmp/nb_conn.last`


#condition s'il y'a + de ligne dans new que dans last alors
if [[ $new -gt $last ]]
then
	echo "diff"
	#creation du body du mail avec 50 dernieres lignes de log interessantes
	tail -n 50 $dir/dionaea.log | grep "accepted connection" > $dir/50lastlines
	python2 $dir/alerting.py
else
	echo "no diff"
fi

#remplacement dans tous les cas de l'ancien par le nouveau
echo $new > /tmp/nb_conn.last