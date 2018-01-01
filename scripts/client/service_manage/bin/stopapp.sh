#!/bin/bash
# Filename: stopapp.sh
# Revision: 1.1
# Date: 2017/02/15
# Email: sheng.huang@bqjr.cn
# Usage: bash stopapp.sh
# 功能：停止应用程序 
# 详细如下：
#     通过用户名和应用安装位置获取到应用运行id号 直接kill，kill过程会列出详细信息
#     脚本运行会检测是否已经过checkapp步骤，否则不会继续执行。
# 返回值： 正常 0；  不正常 1


# 脚本获取绝对路径，使不受运行位置影响
if [ `echo "$0" |grep -c "/"` -gt 0 ];then
    cd ${0%/*}
fi

PROGRAM_DIR=`pwd`
cd ..
BASE_DIR=`pwd`
PROGRAM_NAME=`basename $0`

# 加载运行所需函数库
. ${BASE_DIR}/bin/pub.lib

# 定义目录名变量
TEMP_DIR=${BASE_DIR}/temp
LOG_DIR=${BASE_DIR}/log
CONFIG_DIR=${BASE_DIR}/conf
BIN_DIR=${BASE_DIR}/bin

# 定义文件名变量
LOG_FILE=${LOG_DIR}/${PROGRAM_NAME}.log
APP_CONF=${CONFIG_DIR}/app_config.conf

# 加载文件中的变量
. ${APP_CONF}

# 脚本运行程序入口
main(){
    typeset func=main
    if [ $# -ne 0 ];then
        log_echo "[error]" "${func}" "Parameter error , ${PROGRAM_NAME} no use anyone parameter "
        return 1
    fi
    log_echo "[info] Enter ${func} with successed ." 
    log_echo "[info]" "Starting test program currently running the user"
    
    # 检测当前执行用户非root
    detectionRootUser || return 1

    # 根据容器类型进行操作
    if [ ${apptype[1]} == "tomcat" ];then
        log_echo "[info]" "To stop the tomcat application"
        stopTomcatApply ${user[1]} ${appdir[1]} || return 1
    elif [ ${apptype[1]} == "weblogic" ];then
        log_echo "[info]" "Weblogic container, temporarily does not support automatic exit"  
    else
        log_echo "[info]" "Container type error or temporary does not support, automatic withdrawal"   
    fi
    
    log_echo "[info]" "Exit func ${func} with successed."
    log_echo "[info]" "停止应用成功或未发现java进程 || Stop the application successful or not find Java process "
    return 0 
}

main $* || exit 1

