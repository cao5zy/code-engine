find ./ -name *~ -exec rm -fv {} \;
find ./ -name "#*#" -exec rm -fv {} \;
find ./ -name *.pyc -exec rm -fv {} \;
find ./ -name *.retry -exec rm -fv {} \;
find ./ -name "*~" | xargs -r rm;
