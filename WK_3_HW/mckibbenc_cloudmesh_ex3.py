import cloudmesh

print cloudmesh.shell("cloud on india")
vmname = "mckibbenc_ex3"
print cloudmesh.shell("vm start --cloud=india --image=futuresystems/ubuntu-14.04 --flavor=m1.small --name={0}".format(vmname))
print cloudmesh.shell("vm delete {0} --cloud=india --force".format(vmname))

