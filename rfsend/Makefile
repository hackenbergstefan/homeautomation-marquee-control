all: send433

send433: RCSwitch.o sendv2.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $+ -o $@ -lwiringPi
clean:
	rm *.o send433
