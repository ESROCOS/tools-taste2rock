#!/bin/bash

echo "[TEST 1] Test for taste2rock.py"
echo ""

PYTHONPATH=../python:$PYTHONPATH

echo "[TEST 1] Clear old results"
rm -rf taste2rock_test1
mkdir -p taste2rock_test1
#rm -rf model1
echo "[TEST 1] Done."
echo ""

if [ ! -d model1/binary.c ]; then
    echo "[TEST 1] Building TASTE model"
    cp -r model1_clean model1
    cd model1
    ./build-script.sh
    cd ..
    "[TEST 1] Done."
    echo ""
else
    echo "[TEST 1] TASTE model already built"
    echo ""
fi

echo ""
echo "[TEST 1] Run Rock export: optionally, enter data as requested"
echo ""
../python/taste2rock_generator.py model1/binary.c taste2rock_test1
echo "[TEST 1] Done."
echo ""

echo "[TEST 1] Copy ready-made task implementations"
cp test1_impl/taste2rock_test1_producer*.* taste2rock_test1/taste2rock_test1_producer/tasks/
cp test1_impl/taste2rock_test1_consumer*.* taste2rock_test1/taste2rock_test1_consumer/tasks/
echo "[TEST 1] Done."
echo ""

echo "[TEST 1] Building Rock component: taste2rock_tes1_producer"
cd taste2rock_test1/taste2rock_test1_producer
echo "[TEST 1] in $(pwd)"
amake .
cd ../..
echo "[TEST 1] Done."
echo ""

echo "[TEST 1] Building Rock component: taste2rock_tes1_consumer"
cd taste2rock_test1/taste2rock_test1_consumer
echo "[TEST 1] in $(pwd)"
amake .
cd ../..
echo "[TEST 1] Done."
echo ""

if [ -f taste2rock_test1/start.rb ]; then
    echo "[TEST 1] Launch Rock tasks"
    ruby taste2rock_test1/start.rb
    echo "[TEST 1] Done."
else
    echo "[TEST 1] Startup script not found"
fi
echo ""

echo "[TEST 1] Test Rock tasks installed in the workspace. To cleanup, run:"
echo 'rm -rf `find $AUTOPROJ_CURRENT_ROOT/install -name "*taste2rock_test1_producer*"`'
echo 'rm -rf `find $AUTOPROJ_CURRENT_ROOT/install -name "*taste2rock_test1_consumer*"`'
echo ""
