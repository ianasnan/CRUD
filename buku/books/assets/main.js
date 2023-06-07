function deletebuku(e) {
	var link 	= $(e).attr('alt');
	var id 		= $(e).attr('idnya');
	$.ajax({
		type : "GET",
		url: link,
    	data: {id:id},
		datatype: 'html',
		success: function(e) {
			window.location.reload();
		}
	})
}
function editbuku(e) {
	var link 	= $(e).attr('alt');
	var id 		= $(e).attr('idnya');
	$.ajax({
		type : "GET",
		url: link,
    	data: {id:id},
		datatype: 'json',
		success: function(e) {
			$('#id').val(""+e['id_buku']+"");
			$('#judul').val(""+e['judulbuku']+"");
			$('#deskripsi').val(""+e['deskripsi']+"");
			$('#kategori').val(""+e['kategori']+"");
			$('#keyword').val(""+e['keyword']+"");
			$('#harga').val(""+e['harga']+"");
			$('#penerbit').val(""+e['penerbit']+"");
			$('#myForm').attr("action","editbuku/");
		}
	})
}