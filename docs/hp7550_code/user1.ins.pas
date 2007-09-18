{  PRSVR.INS.PAS, 
   Print server routines and associated data types which
   are exported for user supplied device drivers.

   Changes:
      11/04/86 jjm  Added comments
      10/13/86 jjm  added prf_$orient and prf_$paper_t 
      08/18/86 jjm  added server_db and driver_db sr9.5 info
      03/30/85 jjm  updated for sr9 release
      04/09/84 jjm  update to sr8
      05/09/83 gtr  original coding                  


}
                       
CONST  pr_$bufsize = 2048 ;   


TYPE   pr_$buf_t = ARRAY [1..pr_$bufsize] OF char ;
       pr_$t = (pr_$user1, pr_$user2, pr_$user3, pr_$user4) ;

       pr_$set_op_t = (
                      pr_$font_weight,
                      pr_$font_size,
                      pr_$text_precision,
                      pr_$data_format,
                      pr_$pitch,
                      pr_$y_dimension,
                      pr_$x_dimension,
                      pr_$rep_factor,        
                      pr_$config,
                      pr_$copies,
                      pr_$server_db
                      );
             
       pr_$inq_op_t = (
                         pr_$bpi,
                         pr_$rep_ability,
                         pr_$driver_db
                            );
   
   
       pr_$font_weight_t = (
                              pr_$light,
                              pr_$medium,
                              pr_$bold 
                             );

       pr_$text_precision_t = (
                                 pr_$draft,
                                 pr_$letter_quality
                                );

       pr_$data_format_t = (
                              pr_$text,
                              pr_$plot,
                              pr_$transparent
                                );
                           

       prsvr_color_format_t = (none, {not a color printer}
                                pixel, {color map format}
                                scan_line_rgb,{3 plane formats}
                                scan_line_ymc,
                                plane_rgb,
                                plane_ymc
                                );  {this tells the server how to send bitmap data}

                           
       pr_$interface_t = ( pr_$serial,
                           pr_$parallel,
                           pr_$external,
                           pr_$versatec,
                           pr_$multibus);

        prf_$paper_t = (
                        prf_$cut_sheet,
                        prf_$fan_fold,
                        prf_$roll,
                        prf_$transparency,
                        prf_$null
                        );                

        prf_$orient_t = (
                        prf_$landscape,
                        prf_$portrait 
                        );


(*
    This data structure is set up by PRSVR based on PRF options specified by
    the user and information the driver passes to PRSVR via the return_info call.
    When the setmode call operation type = pr_$server_db , dereference the server_db_ptr_t 
    in pr_$data_rec_t to obtain the current parameters for this job.
    Use these values to format and control how the data is output to the print device.
    Ignore any other operation types (except interface) passed by the set mode call. 
    They exist only for backwards compatability.
*)

        server_db_t = RECORD 
            copies : binteger;
            print_mode : pr_$data_format_t;
            cpi : real; {characters per inch}
            lpi : real; {lines per inch}
            weight : pr_$font_weight_t;
            lq : boolean;
            resolution : pinteger; {set the printer to print at this resolution}
            magnification : integer; {set the printer to magnify a bitmap by this amount}
            bitmap_size : RECORD
                x : integer; {the number of bits PRSVR will send}
                y : integer; 
                planes : integer; {bits per pixel}
                END;
            color : boolean; {this file should be printed in color}
            bw_rev : boolean; {set if user requests it and the printer can do it }
            color_map : UNIV_PTR; {pointer to the gpr bitmap color map}
            page_layout : prf_$orient_t; 
            page_reversal : boolean;
            collate_copies : boolean;
            paper : RECORD
                page_size : RECORD
                    w : REAL;
                    l : REAL;
                    END;
                style : prf_$paper_t;
                END;
        END;

        server_db_ptr_t = ^server_db_t; {this points you to the PRSVR server_db}

(*
     Use this data structure to pass PRSVR information about the driver and
     printers capabilities. PRSVR will issue a return_info call at 
     startup, requesting this information. When the operation type of
     this call = pr_$driver_db , deference driver_db_ptr_t in pr_$data_rec_t
     to pass PRSVR this information.
     Ignore any other operations passed by the return info call. 
     They exist only for backwards compatability.
*)
                                                                

        driver_db_t = RECORD  {information about the printer that the driver supplies}
            valid : boolean; { set this to true }
            copies : boolean; {does the printer do multiple copies}
            cpi : ARRAY [1..10] OF real;  {an array of character spacings}
            lpi : ARRAY [1..10] OF real; 
            resolution : ARRAY [1..4] OF pinteger;
                               { the printer plots at these resolutions}
            res_min : pinteger; {a range of resolutions from minimum ...}
            res_max : pinteger;  {... to maximum}
            magnification : ARRAY [1..16] OF binteger; 
            color_format : prsvr_color_format_t; {tell prsvr how to send
                                                  color images}
            bw_rev : boolean; {set if the printer can bw reverse image}       
            paper : RECORD
                page_size : RECORD
                    w : REAL;
                    l : REAL;
                    END;
                style : prf_$paper_t;
                margins : RECORD {unprintable regions of paper}
                    l,r,t,b : real;
                    END;
                END;
            image_rotation : boolean; {the controller can rotate a bitmap}
            END;                                           

        driver_db_ptr_t = ^driver_db_t; {a pointer to the PRSVR driver_db_t}


                           
       pr_$data_rec_t = packed RECORD
                            font_weight : pr_$font_weight_t ;
                            font_size : real ;
                            text_precision : pr_$text_precision_t ;
                            bpi : RECORD
                                  x : integer ;
                                  y : integer ;
                                  END;
                            data_format: pr_$data_format_t;
                            pitch : real ;
                            x_dimension : pinteger ;
                            y_dimension : pinteger ;
                            rep_factor : pinteger;
                            rep_ability : boolean;
                            copies : pinteger;             
                            interface: pr_$interface_t;
                            server_db_ptr : server_db_ptr_t;
                            driver_db_ptr : driver_db_ptr_t;
                            END ;


{Called once when the print server starts. Open I/O channels in this call}
PROCEDURE user2_init (
               IN  sio_line:  integer;
               IN  sio_speed:  integer
           ) ;  EXTERN ;

PROCEDURE user3_init (
               IN  sio_line:  integer;
               IN  sio_speed:  integer
           ) ;  EXTERN ;


PROCEDURE user4_init (
               IN  sio_line:  integer;
               IN  sio_speed:  integer
           ) ;  EXTERN ;

{Called at program startup. Use only the driver_db operation}
PROCEDURE user2_return_info (
                         IN operation : pr_$inq_op_t;
                         OUT datum : pr_$data_rec_t
                        ); EXTERN ;

PROCEDURE user3_return_info (
                         IN operation : pr_$inq_op_t;
                         OUT datum : pr_$data_rec_t
                        ); EXTERN ;

PROCEDURE user4_return_info (
                         IN operation : pr_$inq_op_t;
                         OUT datum : pr_$data_rec_t
                        ); EXTERN ;

{Called once at startup to set the interface}
{Called at the beggining of each job. Use only the server_db operation to set job parameters}
PROCEDURE user2_set_mode (
                         IN operation : pr_$set_op_t;
                         IN datum : pr_$data_rec_t
                        ); EXTERN ;

PROCEDURE user3_set_mode (
                         IN operation : pr_$set_op_t;
                         IN datum : pr_$data_rec_t
                        ); EXTERN ;

PROCEDURE user4_set_mode (
                         IN operation : pr_$set_op_t;
                         IN datum : pr_$data_rec_t
                        ); EXTERN ;



{called multiple times for each job. This is the data to format and print}
PROCEDURE  user2_write (
               IN  str:  UNIV pr_$buf_t ;
               IN  strlen:  pinteger
           ) ;  EXTERN ;

PROCEDURE  user3_write (
               IN  str:  UNIV pr_$buf_t ;
               IN  strlen:  pinteger
           ) ;  EXTERN ;

PROCEDURE  user4_write (
               IN  str:  UNIV pr_$buf_t ;
               IN  strlen:  pinteger
           ) ;  EXTERN ;


{Called at the end of each job. Reset job specific paramters to default values}
PROCEDURE  user2_flush ;  EXTERN ;

PROCEDURE  user3_flush ;  EXTERN ;

PROCEDURE  user4_flush ;  EXTERN ;


{Called when the print server terminates. Terminate any current jobs and close I/O channels}
PROCEDURE  user2_close ;  EXTERN ;

PROCEDURE  user3_close ;  EXTERN ;

PROCEDURE  user4_close ;  EXTERN ;



%eject ;


