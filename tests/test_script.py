from openvpn_checker import script

script_name = "hello.sh"
my_script = script.Script(script_name)

print(my_script.get_path())
my_script.start_script()
query = raw_input("stop (y/n)")

if query == "y":
    my_script.stop_script()
    print "stopped"
else:
    print "ok then"