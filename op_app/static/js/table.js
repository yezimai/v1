/**
 * Created by hp on 2017/9/29.
 */
$(function(){

    //表格(DataTables)-3，使用对象数据源
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
            next: '下一页'
        }
    };
//    var dataSet2 = [
//        {
//            "city": "深圳",
//            "group": "分组名称888",
//            "time": '8:00 - 18:49',
//            "pass": '52.67%',
//            "7avg": '67.32%',
//            "3avg": '68.98%'
//        }, {
//            "city": "哈尔滨",
//            "group": "分组名称888",
//            "time": '8:00 - 18:49',
//            "pass": '78.37%',
//            "7avg": '73.72%',
//            "3avg": '68.98%'
//        }, {
//            "city": "成都",
//            "group": "分组名称888",
//            "time": '8:00 - 18:49',
//            "pass": '77.67%',
//            "7avg": '76.32%',
//            "3avg": '74.88%'
//        }
//    ];

    var columns = [
        {title : '城市', data: "city"},
        {title : '分组', data: "group", width : 220},
        {title : '时段', data: "time"},
        {title : '通过率(%)', data: "pass"},
        {title : '7日时段均值(%)', data: "7avg"},
        {title : '3日同时段均值(%)', data: "3avg"}
    ];


    function show_data(){
//        var table = $('#table2_demo3').DataTable();
//        table.clear();
        $('#table2_demo3').children().remove();
        $.ajax({
//            async: "false",
            type: 'post',
            url: '/ajget_data/',
            data:{},
            dataType : 'json',
            success:function(data){
//                console.log(data);
                $('#table2_demo3').dataTable({
                    destroy: true,
                    lengthChange: false, //不允许用户改变表格每页显示的记录数
                    searching: false, //关闭搜索
                    language: language, //汉化
                    pageLength : 300, //每页显示几条数据
                    autoWidth: false,
                    data : data,
                    columns : columns
                });
                var table = $('#table2_demo3').DataTable();
                    table
                        .column('3:visible' )
                        .order( 'asc' )
                        .draw();
            },
            error: function (XMLHttpRequest, textStatus, errorThrown){
                console.log("error + textStatus", textStatus);
            }
        });
    }


    show_data();
    if (!handle){
        var handle = setInterval(function(){
            show_data();
        }, 900000);
    }






});