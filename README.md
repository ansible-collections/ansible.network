

# Ansible Network Collection for network and IP utilities that are not specific to any platform or OS, or that interact with any platform os. 
[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/builds?project=ansible-collections%2Fansible.network) <!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/ansible.network)](https://codecov.io/gh/ansible-collections/ansible.network)-->

The Ansible ``ansible.network`` collection includes common content network and IP utilities that are not specific to any platform or OS.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10,<2.11**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

## Included content

<!--start collection content-->

### Test plugins
Name | Description
--- | ---
ansible.netcommon.disabled|Case insensitive test for `disabled`<br/>`interface.ip_redirects is ansible.netcommon.disabled`
ansible.netcommon.down|Case insensitive test for `down`<br/>`interface.oper_state is ansible.netcommon.down`
ansible.netcommon.enabled|Case insensitive test for `enabled`<br/>`interface.bpdu_guard is ansible.netcommon.enabled`
ansible.netcommon.in_any_network|Test if an IP or network is in any network<br/>`'10.1.1.1' is ansible.netcommon.in_any_network ['10.0.0.0/8', '192.168.1.0/24']`
ansible.netcommon.in_network|Test if an address or network is in a network<br/>`'10.1.1.1' is ansible.netcommon.in_network '10.0.0.0/8'`
ansible.netcommon.in_one_network|Test if an IP or network is in one network<br/>`'10.1.1.1' is ansible.netcommon.in_one_network ['10.0.0.0/8', '192.168.1.0/24']`
ansible.netcommon.ip|Test if something in an IP address or network<br/>`'10.1.1.1' is ansible.netcommon.ip`
ansible.netcommon.ip_address|Test if something in an IP address<br/>`'10.1.1.1' is ansible.netcommon.ip_address`
ansible.netcommon.ipv4|Test if something in an IPv4 address or network<br/>`'10.0.0.0/8' is ansible.netcommon.ipv4`
ansible.netcommon.ipv4_address|Test if something in an IPv4 address<br/>`'10.1.1.1' is ansible.netcommon.ipv4_address`
ansible.netcommon.ipv4_hostmask|Test if an address is a hostmask<br/>`'0.0.0.255' is ansible.netcommon.ipv4_hostmask`
ansible.netcommon.ipv4_netmask|Test for a valid IPv4 netmask<br/>`'255.255.255.0' is ansible.netcommon.ipv4_netmask`
ansible.netcommon.ipv6|Test if something is an IPv6 address or network<br/>`'2001:db8:a::123/64' is ansible.netcommon.ipv6`
ansible.netcommon.ipv6_address|Test if something is an IPv6 address<br/>`'fe80::216:3eff:fee4:16f3' is ansible.netcommon.ipv6_address`
ansible.netcommon.ipv6_ipv4_mapped|Test if something appears to be a mapped IPv6 to IPv4 mapped address<br/>`'::FFFF:10.1.1.1'' is ansible.netcommon.ipv4_ipv4_mapped`
ansible.netcommon.ipv6_sixtofour|Test if something appears to be a 6to4 address<br/>`'2002:c0a8:6301:1::1' is ansible.netcommon.ipv6_sixtofour`
ansible.netcommon.ipv6_teredo|Test if something is an IPv6 teredo address<br/>`'2001::c0a8:6301:1' is ansible.netcommon.ipv6_teredo`
ansible.netcommon.loopback|Test if an IP address is a loopback<br/>`'127.10.10.10' is ansible.netcommon.loopback`
ansible.netcommon.mac|Test if something appears to be a valid mac address<br/>`'02:16:3e:e4:16:f3' is ansible.netcommon.mac`'
ansible.netcommon.multicast|Test for a multicast IP address<br/>`'224.0.0.1' is ansible.netcommon.multicast`
ansible.netcommon.private|Test if an IP address is private<br/>`'10.1.1.1' is ansible.netcommon.private`
ansible.netcommon.public|Test if an IP address is public<br/>`'8.8.8.8' is ansible.netcommon.public`
ansible.netcommon.reserved|Test for a reserved IP address<br/>`'253.0.0.1' is ansible.netcommon.reserved`
ansible.netcommon.resolvable|Test if an IP or name can be resolved via /etc/hosts or DNS<br/>`'docs.ansible.com' is ansible.netcommon.resolvable`
ansible.netcommon.subnet_of|Test if a network is a subnet of another network<br/>`'10.1.1.0/24' is ansible.netcommon.subnet_of '10.0.0.0/8'`
ansible.netcommon.supernet_of|Test if an network is a supernet of another network<br/>`'10.0.0.0/8' is ansible.netcommon.supernet_of '10.1.1.0/24'`
ansible.netcommon.unspecified|Test for a unicast IP address<br/>`'0.0.0.0' is ansible.netcommon.unspecifed`
ansible.netcommon.up|Case insensitve test for `up`<br/>`interface.admin_state is ansible.netcommon.up`

<!--end collection content-->


## Installing this collection

You can install the ``ansible.network`` collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install ansible.network

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ansible.network
```
## Using this collection

**NOTE**: For Ansible 2.9, you may not see deprecation warnings when you run your playbooks with this collection. Use this documentation to track when a module is deprecated.

### See Also:

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [ansible.network collection repository](https://github.com/ansible-collections/ansible.network). See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for complete details.

You can also join us on:

- Freenode IRC - ``#ansible-network`` Freenode channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.


## Release notes
<!--Add a link to a changelog.md file or an external docsite to cover this information. -->

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Developing network resource modules](https://docs.ansible.com/ansible/latest/network/dev_guide/developing_resource_modules_network.html#developing-resource-modules)
- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
