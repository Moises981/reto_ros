execute_process(COMMAND "/home/rog-strix/Desktop/reto_playtec_ws/build/bb8_arduino/rosserial/rosserial_vex_v5/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/rog-strix/Desktop/reto_playtec_ws/build/bb8_arduino/rosserial/rosserial_vex_v5/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
