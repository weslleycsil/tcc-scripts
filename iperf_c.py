import iperf3
import json

client = iperf3.Client()
client.duration = 1
client.server_hostname = '150.162.9.156'
client.protocol = 'udp'
result = client.run()

#

if result.error:
    print(result.error)
else:
    print('')
    #print(result.json)
    #data = result.json
    #print(data['start'])
    print('Test completed:')
    #print('  started at         {0}'.format(result.time))
    #print('  bytes transmitted  {0}'.format(result.bytes))
    #print('  jitter (ms)        {0}'.format(result.jitter_ms))
    #print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))

    #print('Average transmitted data in all sorts of networky formats:')
    #print('  bits per second      (bps)   {0}'.format(result.bps))
    #print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
    #print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
    #print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
    #print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))

    print(result)