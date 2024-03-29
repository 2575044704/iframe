from sshtunnel import SSHTunnelForwarder
import paramiko
import time
#install_Frpc('5140',frpconfigfile,use_frpc)
# SSH 连接参数
ssh_host = 'ssh.intern-ai.org.cn'
ssh_port = 39126
ssh_username = 'root'
ssh_password = 'U76nhtaiygoV7No6'

# 本地端口映射参数
local_host = 'localhost'
local_port = 7860

# 远程端口
remote_host = 'localhost'  # 这里假设远程服务器上要映射的端口是localhost
remote_port = 7860

try:
    # 创建 SSH 端口转发器
    with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=(remote_host, remote_port),
        local_bind_address=(local_host, local_port)
    ) as tunnel:
        print(f"SSH tunnel established from {local_host}:{local_port} to {remote_host}:{remote_port}")

        # 保持 tunnel 活跃
        tunnel.start()
        os.system("curl http://127.0.0.1:7860")
        # 在此处添加需要执行的操作，tunnel 会在此期间保持活跃状态
        time.sleep(9999999)
except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials.")
except paramiko.SSHException as ssh_exception:
    print(f"Unable to establish SSH connection: {ssh_exception}")
except Exception as e:
    print(f"An error occurred: {e}")
