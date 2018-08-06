$(function(){
    $('#option2-1').attr('checked','checked');
    $('#opt2-label1').removeClass('btn-default')
    .addClass('on');
    $('input:radio[name="options-2"]').on('change',function(){
        $(this).parent().removeClass('btn-default')
            .addClass('on').siblings().removeClass('on')
            .addClass('btn-default');
    })
    $('#option3-1').attr('checked','checked');
    $('#opt3-label1').removeClass('btn-default')
    .addClass('on');
    $('input:radio[name="options-3"]').on('change',function(){
        $(this).parent().removeClass('btn-default')
            .addClass('on').siblings().removeClass('on')
            .addClass('btn-default');
    });
    $('#sub-Btn').on("click",function (){
        var form={};
        form['select-1'] = $('select[name="select-1"] option:selected').val();
        form['select-2'] = $('select[name="select-2"] option:selected').val();
        form['select-3'] = $('select[name="select-3"] option:selected').val();
        form['select-4'] = $('select[name="select-4"] option:selected').val();
        form['select-5'] = $('input:radio[name="options-2"]:checked').val();
        form['select-6'] = $('input:radio[name="options-3"]:checked').val();
        console.log(form);
        $.ajax({
            url:"/crawl/",
            type:"POST",
            data: form,
            datatype:'json',
            success:function(data){
                console.log(data);
            },
            error:function(){
                $('mainimg').attr('src','/static/pic/comic.jpg');
            }
        })
    }); 
}
);
