$(function(){

    var g_val = {
        'env_id': '',
        'app_id': '',
    }

    var language = {
        search: '搜索：',
        lengthMenu: "每页显示 _MENU_ 记录",
        zeroRecords: "没找到相应的数据！",
        info: "分页 _PAGE_ / _PAGES_",
        infoEmpty: "暂无数据！",
        infoFiltered: "(从 _MAX_ 条数据中搜索)",
        paginate: {
        first: '首页',
        last: '尾页',
        previous: '上一页',
        next: '下一页',
        }
    }

    // 显示host 主机信息
//    function show_datatable(){
//    }
    $("#table2_demo4").dataTable({
        autoWidth: false,
        lengthChange: true, //不允许用户改变表格每页显示的记录数
        pageLength : 5, //每页显示几条数据
        lengthMenu: [5, 10, 20], //每页显示选项
        pagingType: 'full_numbers',
        //ajax : '/op/hostInfo/?project_id='+ $('#project_id').val() +'&env_id=' + g_val.env_id + '&app_id='+g_val.app_id,
        ordering: true,
        columns : [
          {data:"ip", orderable: true},
          {data:"env_name"},
          {data:"manager"},
          {
            data: null,
            orderable: false,
            render : function(data, type, row, meta){
                btn_html = `
                    <a target="_blank"  class="king-btn king-radius king-info click-btn" value="start" >启动</a>
                    <a target="_blank"  class="king-btn king-radius king-danger click-btn" value="stop" >停止</a>

                    <div class="btn-group" role="group">
                        <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          更改操作
                          <span class="caret"></span>
                        </button>
                        <ul class="dropdown-menu">
                          <li><a target="_blank" class="click-btn" value="log_show" href="#">日志查看</a></li>
                          <li><a target="_blank" class="click-btn" value="task_manage" href="#">任务管理</a></li>
                          <li><a target="_blank" class="click-btn" value="run_command" href="#">命令执行</a></li>
                          <li><a target="_blank" class="click-btn" value="machine_detail" href="#">机器详情</a></li>
                        </ul>
                    </div>`
                return btn_html;
            }
          }
        ],
        language:language
    });

    var t = $("#table2_demo4").DataTable();  // 获取datatables对象
    $("#table2_demo4 tbody").on('click', 'a.click-btn', function(e){
        var _this = this
        var row = t.row( $(_this).parents('tr') ), // 获取按钮所在的行
            data = row.data();
        console.log('data:', data);
        var action_value = $(_this).attr('value');
        console.log('action_value:', action_value);
        var action_params = '?project_id='+ $('#project_id').val() + '&env_id=' + g_val.env_id + '&app_id=' + g_val.app_id + '&ip='+ data.ip +'&action=' + action_value;
        if (action_value == 'start' || action_value == 'stop' ){
            if(confirm('确定要' + action_value + ' ?')){
                $.ajax({
                    type:'POST',
                    url : '/op/doServiceManageAction/',
                    data : {
                        project_id : $('#project_id').val(),
                        env_id :  g_val.env_id,
                        app_id :  g_val.app_id,
                        ip :  data.ip,
                        action :  action_value,
                    },
                    beforeSend:function(jqXR, settings){
                        $(_this).attr('href', '/op/getLogDetail/' + action_params);
                        $.messager.progress();
                    },
                    success:function(data){
                        $.messager.progress('close');
                        console.log(data);
                    },
                    error : function(XMLHttpRequest, textStatus, errorThrown) {
                        $.messager.progress('close');
                        $.messager.show({
                            title:'提示',
                            msg:'操作失败！，错误信息：' + errorThrown,
                            showType: 'slide',
                            timeout: 3000
                        });
                    },
                });
            }
//        }else if (action_value == 'log_show'){  // 日志查看
//            $(this).attr('href', action_url);
//        }else if (action_value == 'task_manage'){ //  任务管理
//            $(this).attr('href', action_url);
//        }else if (action_value == 'run_command'){  // 运行命令
//            $(this).attr('href', action_url);
//        }else if (action_value == 'machine_detail'){ // 机器详情
//            $(this).attr('href', action_url);
        }else{
            var action_url = '/op/doFunctionPage/' + action_params;
            $(this).attr('href', action_url);
        }




    });

    // 环境类型按钮点击
    $('.env-type').bind('click', '.env-type', function(e){
        var _this = this;
        g_val.env_id = $(_this).attr('value');
        console.log('select env_id:', g_val.env_id);
        $(_this).removeClass('king-success')
        // 更改选中效果
        $(_this).parent().find('.my-btn').each(function(i){
            if ($(this).html() != $(_this).html()){
                $(this).removeClass('king-success').addClass('king-success');
            }
        });
    });

    // 应用按钮选择
    $('.app-name').bind('click', '.app-name', function(e){
        var _this = this;
        g_val.app_id = $(_this).val();
        console.log('select appid:', g_val.app_id);
        $(_this).removeClass('king-info');
        $(_this).parent().find('.my-btn').each(function(i){
            if ($(this).val() != $(_this).val()){
                $(this).removeClass('king-info').addClass('king-info');
            }
        });

        // 显示 table 表格
        $('.detail-list').css({
            'display': 'block'
        });

        // 重新获取数据
        var t = $("#table2_demo4").DataTable();  //获取datatables对象
        ajax_url ='/op/hostInfo/?project_id='+ $('#project_id').val() +'&env_id=' + g_val.env_id + '&app_id=' + g_val.app_id;
        t.ajax.url(ajax_url).load();


        // ajax 获取主机信息


    });



});
