$(function(){

    $('#nav').tree({
        url : '/op/getNav/',
        lines:true,
        onClick:function(node){      // 点击事件处理
//            console.log(node);
            var tabs = $('#tabs').tabs();
            for (var i=0;i<tabs.length;i++){
                if($('#tabs').tabs('exists', i)){
                    $('#tabs').tabs('close', i);
                }
            }

            if(!node.children){                     // 没有子节点的点击
                if ($('#tabs').tabs('exists', node.text)){
                    $('#tabs').tabs('select', node.text);
                }else{
                    $('#tabs').tabs('add', {
                        title : node.text,
                        closable:true,
                        href: node.url + '?node_id='+ node.id,
                    });
                }
            }
        },
    });


    $('#tabs').tabs({
        fit:true,
    });

});
